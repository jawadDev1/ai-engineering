# Langchain

Langchain is an open source framework for building LLM based application like chatbot, autonomous agents etc.

## Benefits
1. Chains - hepls build piplines. we can use sequential chains where one chain result become another chains input. And we can also use parallal chains
2. Model Agnostic Development - It allows to use multiple models like gpt, claude.
3. Complete ecosystem - it provides document loader, text splitters etc
4. Memory state handling - provides memory so model can have context

## Uses/Applications
1. Chatbots
2. Knowledge Assistent
3. AI Agents
4. Workflow Automation
5. Summarization/Research Helpers

## Components
### 1. Models
Model component provides an interface to communication with different LLM models like gpt, claude gemini etc.

### 2. Prompts
Prompt is basically the input provided to LLM. Langchain helps in creating different types of prompt. For example
1. Dynamic & Reuseable prompt
2. Role based prompt
3. Few-shot prompt

### 3. Chains
Chains hepls us build pipelines. For example let's say we have a pipeline which converts the user paragraph into German and then summarize that paragraph into 100 words
```
Input ---> LLM ---> translated input ---> LLM ---> summarized text. 
```
This is a squential chain. we can also have parallel chains

### 4. Indexes
Indexes connect the model to external knowledge such as documents, databases etc. Indexes consists of 4 things, Document loaders, text-splitters, vector store, retriver

### 5. Memory
LLM API calls are stateless. Langchain helps us use memory, so LLM can have access to previous conversations. We have different types of memories
1. Conversation Buffer Memory - stores a transcript of recent messages. Great for short chats but can grow quickly.
2. Conversation-Buffer-Window-Memory - Only keeps the last n interactions (conversations) to avoid excessive token usage.
3. Summarized-Based Memory - Periodically summarizes old chat segments to keep a condensed  memeory footprint
4. Custom Memory - for advance cases, store specialized state

### 6. Agents
Langchain also allows to create agents. Agents can perform certain tasks, for example booking a flight, ordering a product, getting latest weather etc. AI agent has two main capabilities reasoning and tools
