from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import  BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import sqlite3



load_dotenv()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.5 
)


def chat_node(state: ChatState):
    messages = state['messages']

    res = llm.invoke(messages)

    return {'messages': [res]}

conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

# Retrieve threads from database
def get_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)
