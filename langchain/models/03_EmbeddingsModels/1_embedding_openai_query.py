from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# Generate vector of 32 dimension
result = embedding.embed_query("Islamabad is the capital of pakistan")

print(str(result))
