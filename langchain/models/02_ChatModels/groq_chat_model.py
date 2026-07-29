from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")

result = model.invoke("What is the capital of german?")

print(result.content)
