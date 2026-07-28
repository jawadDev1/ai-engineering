# Structured Output

In Langchain, structured output refers to the practice of having language models return a response in a well-defined data format.

There are two type of LLMs , the one which are trained and can give you structured output like GPT, calude etc, there are some other llms as well which can not give you structured output but langchain gives you output parser for parsing these lllms output into a structure format.

Use cases:

1. Data Extraction
2. API Building
3. Agents

3 ways of formatting structure

1. Typed Dict
2. Pydantic
3. JSON Schema

## With Structred Output

with_structured_output function generates a prompt and sends it along with the user prompt to get response in a structured format

### TypedDict

TypedDict is a way to define a dictionary in python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure. If you know typescript it's similar to Interface or type
