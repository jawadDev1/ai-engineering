from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.7 
)

messages = [
    SystemMessage(content="You are a helpful assistent"),
    HumanMessage(content="Tell me about langchain in 2 lines"),
]

result = model.invoke(messages)

messages.append(AIMessage(result.content) )

print(messages)