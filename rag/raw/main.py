import os
import time
import uuid  # every record in vector db will have an id
from pathlib import Path
from typing import Any, Dict, List, Tuple

import chromadb

# for Embedding & Vector db
import numpy as np
from chromadb.config import Settings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader
from langchain_core.documents import Document

# GROQ LLM
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer  # embedding model
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# Data Ingession to Vector DB Pipeline


# Read all the pdfs inside the dir
def process_all_pdfs(pdf_path):
    """Process all pdf files in a directory"""
    all_docs = []

    pdf_dir = Path(pdf_path)

    # Find all pdf files recursively
    pdf_files = list(pdf_dir.glob("**/*.pdf"))

    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        print(f"\n Processing: {pdf_file.name}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()

            # Add source info to metadata
            for doc in docs:
                doc.metadata["source_file"] = pdf_file.name
                doc.metadata["file_type"] = "pdf"

            all_docs.extend(docs)

            print(f"Loaded {len(docs)} pages")
        except Exception as e:
            print(f"Failed to load doc: {e}")

    print(f"Total Documents loaded: {len(all_docs)}")
    return all_docs


# Text splitting get into chunks
def split_docs(docs, chunk_size=1000, chunk_overlap=200):
    """Split document into smaller chunks for better RAG performance"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )

    split_docs = text_splitter.split_documents(docs)
    print(f"Split {len(docs)} docs into {len(split_docs)} chunks")

    if split_docs:
        print("\nExample chunk:")
        print(f"\nContent: {split_docs[0].page_content[:200]}...")
        print(f"\nMetadata: {split_docs[0].metadata}...")

    return split_docs


# Embedding & Vector Store DB
class EmbeddingManager:
    """Handles Document embedding generation using SentenceTransformer"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding manager
        Args:
            model_name: HuggingFace model name for sentence embeddings
        """

        self.model_name = model_name
        self.model = None
        self._load_model()  # _ => protected function

    def _load_model(self):
        """Load the SentenceTransformer model"""
        try:
            print(f"Loading embedding model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            print(
                f"Model loaded successfully. Embedding dimension: {self.model.get_sentence_embedding_dimension()}"
            )
        except Exception as e:
            print(f"Error loading model {self.model_name}: {e}")
            raise

    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts

        Args:
            texts: List of texts to embed
        Returns:
            numpy array of embeddings with shape (len(texts), embedding_dim)
        """

        if not self.model:
            raise ValueError("Model not loaded")

        print(f"Generating embeddings for {len(texts)} texts...")
        embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"Generated embeddings with shape: {embeddings.shape}")
        return embeddings

    def get_embedding_dimension(self) -> int:
        """Get the embedding dimension of the model"""
        if not self.model:
            raise ValueError("Model not found")
        return self.model.get_sentence_embedding_dimension()


# Vector Store
class VectorStore:
    """Manages document embeddings in Chromadb vector store"""

    def __init__(
        self,
        collection_name: str = "pdf_documents",
        presist_directory: str = "data/vector_store",
    ) -> None:
        """
        Initialize the vector store

        Args:
            collection_name: Name of the ChromaDB collection
            presist_directory: directory to presist the vector store
        """

        self.collection_name = collection_name
        self.presist_directory = presist_directory
        self.client = None
        self.collection = None
        self._initialize_store()

    def _initialize_store(self):
        """Initialize ChromaDB client and collection"""
        try:
            # Create presisten ChromaDB client
            os.makedirs(self.presist_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.presist_directory)

            # Get or create collectoin
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"description": "PDF document embeddings for RAG"},
            )
            print(f"Vector store initialized. Collection: {self.collection_name} ")
            print(f"Existing documents in Collection: {self.collection.count()} ")

        except Exception as e:
            print(f"Error initializing vector store: {e}")
            raise

    def add_docs(self, docs: List[Any], embeddings: np.ndarray):
        """
        Add documents and their embeddings to the vector store
        Args:
            docs: List of Langchain documents
            embeddings: Corresponding embeddings for the documents
        """

        if len(docs) != len(embeddings):
            raise ValueError("Number of documents must match number of embeddings")

        print(f"Adding {len(docs)} documents to vector store...")

        # Prepare data for chromadb
        ids = []
        metadatas = []
        docs_text = []
        embeddings_list = []

        for i, (doc, embedding) in enumerate(zip(docs, embeddings)):
            # Generate unique id
            doc_id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(doc_id)

            # Prepare metadata
            metadata = dict(doc.metadata)
            metadata["doc_index"] = i
            metadata["content_length"] = len(doc.page_content)
            metadatas.append(metadata)

            # Document content
            docs_text.append(doc.page_content)

            # Embeddings
            embeddings_list.append(embedding.tolist())

            # Add to collection
            if not self.collection:
                raise ValueError("Collection is not initialized")

        try:
            self.collection.add(
                ids=ids,
                embeddings=embeddings_list,
                metadatas=metadatas,
                documents=docs_text,
            )

            print(f"Successfully added {len(docs)} documents to vector store")
            print(f"Total documents in collection: {self.collection.count()}")
        except Exception as e:
            print(f"Error adding documents to vector store: {e}")
            raise


# RAG Retriever Pipeline
class RAGRetriever:
    """Handles query based retrievel from vector store"""

    def __init__(
        self, vector_store: VectorStore, embedding_manager: EmbeddingManager
    ) -> None:
        """
        Initialize the retriever
        Args:
            vector_store: Vector store containing document embeddings
            embedding_manager: manager for generating query embeddings
        """

        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(
        self, query: str, top_k: int = 5, score_threshold: float = 0.0
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevent documents for a query
        Args:
            query: The search query
            top_k: number of top results to return
            score_threshold: minimum similarity score threshold

        Returns:
            List of dictionaries containing retrieved documents and metadata
        """
        print(f"Retrieving documments for query: '{query}'")
        print(f"Top K: {top_k}, Score threshold: {score_threshold}")

        # Generate query embedding
        query_embedding = self.embedding_manager.generate_embeddings([query])[0]

        # Search in vector store
        try:
            results = self.vector_store.collection.query(
                query_embeddings=[query_embedding.tolist()], n_results=top_k
            )

            retrieved_docs = []

            if results["documents"] and results["documents"][0]:
                documents = results["documents"][0]
                metadatas = results["metadatas"][0]
                distances = results["distances"][0]
                ids = results["ids"][0]

                for i, (doc_id, doc, metadata, distance) in enumerate(
                    zip(ids, documents, metadatas, distances)
                ):
                    # Convert distance to similarity score (ChromaDB uses cosine distance)
                    similarity_score = 1 - distance

                    if similarity_score >= score_threshold:
                        retrieved_docs.append(
                            {
                                "id": doc_id,
                                "content": doc,
                                "metadata": metadata,
                                "similarity_score": similarity_score,
                                "distance": distance,
                                "rank": i + 1,
                            }
                        )
                print(f"Retrieved {len(retrieved_docs)} documents (after filtering)")
            else:
                print("No documents found")

            return retrieved_docs
        except Exception as e:
            print(f"Error during retrievel: {e}")
            return []


# Initialize the Groq LLM
groq_api_key = os.getenv("GROQ_API_KEY")


def rag_simple(query, retriever, llm, top_k=3):
    # Retrive the context
    results = retriever.retrieve(query, top_k)

    context = "\n\n".join([doc["content"] for doc in results]) if results else ""

    if not context:
        return "no relevent context found"

    # Generate the answer
    prompt = f"""
    Use the following context in ``` delimeters, to answer the question concisely.
    Context: ```{context}```

    Question: {query}

    Answer:
    """

    res = llm.invoke([prompt.format(context=context, query=query)])
    return res.content


def rag_advanced(query, retriever, llm, top_k=5, min_score=0.2, return_context=False):
    """
    RAG pipeline with extra features:
        - Returns answer, sources, confidence score, and optionally full context
    """
    results = retriever.retrieve(query, top_k, score_threshold=min_score)

    if not results:
        return {
            "answer": "No relavent context found",
            "sources": [],
            "confidence": 0.0,
            "context": "",
        }

    # Prepare context and sources
    context = "\n\n".join([doc["content"] for doc in results])
    sources = [
        {
            "source": doc["metadata"].get(
                "source_file", doc["metadata"].get("source", "unknown")
            ),
            "page": doc["metadata"].get("page", "unknown"),
            "score": doc["similarity_score"],
            "preview": doc["content"][:300] + "...",
        }
        for doc in results
    ]

    confidence = max([doc["similarity_score"] for doc in results])

    prompt = f"""
    Use the following context in ``` delimeters, to answer the question concisely.
    Context: ```{context}```

    Question: {query}

    Answer:
    """
    res = llm.invoke([prompt.format(context=context, query=query)])
    output = {"answer": res.content, "sources": sources, "confidence": confidence}

    if return_context:
        output["context"] = context

    return output


class AdvancedRAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm
        self.history = []  # Store query history

    def query(
        self,
        question: str,
        top_k: int = 5,
        min_score: float = 0.2,
        stream: bool = False,
        summarize: bool = False,
    ) -> Dict[str, Any]:
        # Retrieve relevant documents
        results = self.retriever.retrieve(
            question, top_k=top_k, score_threshold=min_score
        )
        if not results:
            answer = "No relevant context found."
            sources = []
            context = ""
        else:
            context = "\n\n".join([doc["content"] for doc in results])
            sources = [
                {
                    "source": doc["metadata"].get(
                        "source_file", doc["metadata"].get("source", "unknown")
                    ),
                    "page": doc["metadata"].get("page", "unknown"),
                    "score": doc["similarity_score"],
                    "preview": doc["content"][:120] + "...",
                }
                for doc in results
            ]
            # Streaming answer simulation
            prompt = f"""Use the following context to answer the question concisely.\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"""
            if stream:
                print("Streaming answer:")
                for i in range(0, len(prompt), 80):
                    print(prompt[i : i + 80], end="", flush=True)
                    time.sleep(0.05)
                print()
            response = self.llm.invoke(
                [prompt.format(context=context, question=question)]
            )
            answer = response.content

        # Add citations to answer
        citations = [
            f"[{i + 1}] {src['source']} (page {src['page']})"
            for i, src in enumerate(sources)
        ]
        answer_with_citations = (
            answer + "\n\nCitations:\n" + "\n".join(citations) if citations else answer
        )

        # Optionally summarize answer
        summary = None
        if summarize and answer:
            summary_prompt = f"Summarize the following answer in 2 sentences:\n{answer}"
            summary_resp = self.llm.invoke([summary_prompt])
            summary = summary_resp.content

        # Store query history
        self.history.append(
            {
                "question": question,
                "answer": answer,
                "sources": sources,
                "summary": summary,
            }
        )

        return {
            "question": question,
            "answer": answer_with_citations,
            "sources": sources,
            "summary": summary,
            "history": self.history,
        }


def main():
    # docs = process_all_pdfs("data")
    # chunks = split_docs(docs)
    # print("Done", chunks)

    # Initialize the embedding manager
    embedding_manager = EmbeddingManager()
    vectorstore = VectorStore()

    # texts = [doc.page_content for doc in chunks]

    # embeddings = embedding_manager.generate_embeddings(texts)

    # vectorstore.add_docs(chunks, embeddings)

    rag_retriever = RAGRetriever(
        vector_store=vectorstore, embedding_manager=embedding_manager
    )

    # query_embedding = rag_retriever.retrieve("What is single attention")
    # print(query_embedding)

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0.1,
        max_tokens=1024,
    )

    # answer = rag_simple("What is single attention?", rag_retriever, llm)
    # result = rag_advanced(
    #     "What is single attention?",
    #     rag_retriever,
    #     llm,
    #     top_k=3,
    #     min_score=0.1,
    #     return_context=True,
    # )
    # print("Answer: ", result["answer"])
    # print("Sources: ", result["sources"])
    # print("Confidence: ", result["confidence"])
    # print("Context Preview: ", result["context"][:300])

    adv_rag = AdvancedRAGPipeline(rag_retriever, llm)
    result = adv_rag.query(
        "what is attention is all you need",
        top_k=3,
        min_score=0.1,
        stream=True,
        summarize=True,
    )
    print("\nFinal Answer:", result["answer"])
    print("Summary:", result["summary"])
    print("History:", result["history"][-1])


if __name__ == "__main__":
    main()
