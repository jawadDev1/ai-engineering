
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.5 
)

chat_history = [
    SystemMessage(content='You are a helpful ai assistent'),
]

while True:
    user_input = input("You: ")

    if user_input.lower() in {"exit", "quit"}:
        break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Bot: {response.text}\n")

print(chat_history)