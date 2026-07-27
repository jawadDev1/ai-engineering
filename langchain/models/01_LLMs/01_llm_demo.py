from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("what is the capital of pakistan")

print(result)
