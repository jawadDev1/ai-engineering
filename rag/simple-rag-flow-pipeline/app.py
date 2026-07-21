from data_loader import load_all_documents
from embedding import EmbeddingPipeline
from search import RAGSearch
from vectorstore import FaissVectorStore

if __name__ == "__main__":
    # docs = load_all_documents("../../data")
    # embedding_manager = EmbeddingPipeline()
    # chunks = embedding_manager.chunk_documents(docs)
    # embeddings = embedding_manager.embed_chunks(chunks)

    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()
    # print(store.query("what is single attention?", top_k=3))
    rag_search = RAGSearch()
    query = "What is multi head attention?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary: ", summary)

    # print(embeddings)
