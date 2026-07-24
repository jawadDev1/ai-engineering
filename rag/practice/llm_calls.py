import os
from typing import Dict, List

# For multiple messages
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_groq import ChatGroq

ROLE_MAP = {
    "system": SystemMessage,
    "user": HumanMessage,
    "assistant": AIMessage,
}


def generate_with_single_input(
    prompt: str,
    role: str = "user",
    top_p: float = 3.0,
    temperature: float = 0.5,
    max_tokens: int = 500,
    model: str = "llama-3.3-70b-versatile",
    groq_api_key: str = "",
    **kwargs,
):
    if groq_api_key is None:
        groq_api_key = os.getenv("GROQ_API_KEY")

    if groq_api_key is None:
        raise ValueError(
            "No GROQ_API_KEY provided. Pass groq_api_key or set the GROQ_API_KEY environment variable."
        )

    llm = ChatGroq(
        model=model,
        api_key=groq_api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        model_kwargs={
            # **({"top_p": top_p} if top_p is not None else {}),
            **kwargs,
        },
    )

    response = llm.invoke(prompt)

    return {
        "role": "assistant",
        "content": response.content,
    }


def generate_with_multiple_input(
    messages: List[Dict],
    top_p: float = 3.0,
    temperature: float = 0.5,
    max_tokens: int = 500,
    model: str = "llama-3.3-70b-versatile",
    groq_api_key: str = "",
    **kwargs,
):
    if groq_api_key is None:
        groq_api_key = os.getenv("GROQ_API_KEY")

    if groq_api_key is None:
        raise ValueError(
            "No GROQ_API_KEY provided. Pass groq_api_key or set the GROQ_API_KEY environment variable."
        )

    llm = ChatGroq(
        model=model,
        api_key=groq_api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        model_kwargs={
            # **({"top_p": top_p} if top_p is not None else {}),
            **kwargs,
        },
    )

    lc_messages = [ROLE_MAP[msg["role"]](content=msg["content"]) for msg in messages]

    response = llm.invoke(lc_messages)

    return {
        "role": "assistant",
        "content": response.content,
    }
