from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Islamabad is the capital of pakistan",
    "Berlin is the capital of Germany",
    "Paris is the capital of France",
]

# Generate vector of 32 dimension
result = embedding.embed_documents("Islamabad is the capital of pakistan")

print(str(result))
