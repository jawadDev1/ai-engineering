from langchain_huggingface import HuggingFaceEmbeddings


text = "Islamabad is the capital of pakistan"

documents = [
    "Islamabad is the capital of pakistan",
    "Berlin is the capital of Germany",
    "Paris is the capital of France",
]


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vector = embedding.embed_query(text)
vectors = embedding.embed_documents(documents)
print(str(vectors))
