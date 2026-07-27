from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1, max_completion_tokens=50)

result = model.invoke("what is capital of germany")

print(result.content)
