from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import  BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


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


checkpointer =InMemorySaver()
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)