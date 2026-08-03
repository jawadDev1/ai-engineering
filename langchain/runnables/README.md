# Runnables

## Chains

In langchain we have many individual component like LLM call component, PropmtTemplate , vector store etc, so to connect two component like Prompt Template and LLM call, the langchain team created chains Sequential Chain, and similarly they created many more chains for different use cased and components. But there was a problem, the code base became very big. Because they did not standardized any component, each component was behaving differently, with different standards so they need to write custom code to connect two components called chains.

## Runnable

A runnable is a unit of work. Each unit has the following characteristics

- each runnable can take an input, process data and give an output
- invoke method to call the runnable
- stream method

so basically the langchain standardized the individual component into runnables. Runnables are designed in such a way that they can connect with each other easily, for example if you connect prompt | llm, the prompt output will automatically become the input of llm. Even the workflow you create by connecting different runnables, that workflow also becomes a runnable.
