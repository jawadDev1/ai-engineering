# RAG - Retrievel Augmented Generation

| Section | Description |
|---|---|
| [01 Project](./01_project) | RAG project embedds Documents (pdf, txt etc) into ChromaDB and answers user query using llm and documents context |
| [Practice](./practice) | Practice Code (Document loaders, llm call utils, simple rag flow etc) |


RAG improves the LLM models by giving them information that they don't have in training.

## Retriever
Retriever job is to find the documents relavent to users query

Two search approaches:
1. Keyword Search: Looks for documents containing the exact words as user prompt
2. Semantic Search: Look for documents with similar meaning

## Search
### Metadata Filtering
Uses rigid criteria to filter the documents based on metadata like title, author, creation date, access privileges and more.

### Keyword Search
Retrieves documents where words match the user prompt. The order of words does not matter.
The basic TC scoring treats all the words equally, weather they're common filler words or rare, meaningfull terms.

#### TF (Term Frequency):
The TF technique is simply count how many words are matched in a document. For examplw user prompt has javascript, it checks how many times javascript occures in a document and narrow down documents or gives score to document based on that.
But it also has a problem, the common words such as 'the', 'and' etc get the same value even thoug they can occure a lot of times in a document even if the document does not contain the main user prompt words.

#### TF-IDF (Term Frequency Inverse document frequency):
TF-IDF improves TF by giving less importance to common words and more importance to rare, informative words.

It combines:

TF → How often a word appears in a document.
IDF (Inverse Document Frequency) → How rare that word is across all documents.

For example, in a collection of programming articles:

"the" appears everywhere → very low importance.
"LangGraph" appears in only a few documents → high importance.

So a document containing "LangGraph" is ranked higher than one containing many common words.

#### BM25 (Best matching 25version)
BM25 is an improved version of TF-IDF, and it is also the most used keyword search algorithm. It ranks based on
1. How often the word appears in document
2. How rare those words are accross all documents
3. Document length, so long document don't get unfair advantage

### Semantic search
Matches documents based on the relavent meaning. Both the prompt and document are converted to vectors, then vectors are compared to generate scores.

## Chunking Strategies

### Recursive Text Splitter
The Recursive Character Text Splitter tries to keep the text as natural and meaningful as possible by splitting in stages.
For example, if you set chunk_size = 100:
It tries these separators in order:

1. Paragraph (\n\n)
2. Line (\n)
3. Sentence/punctuation or space
4. Character

Suppose you have:
```
Paragraph 1...

Paragraph 2...

Paragraph 3...
```

If Paragraph 1 is under 100 characters, it keeps it as one chunk.
If Paragraph 1 is 300 characters, it tries to split by new lines.
If there are no new lines, it tries spaces.
If even that isn't enough (e.g., a long string), it finally splits by characters.

### Document Text Splitter
A Document Text Splitter (or document-aware splitter) understands the structure of the document, not just characters. For example, a Markdown document:
```
# Introduction

...

# Installation

...

# API

...
``` 

A document-aware splitter will keep each section together instead of cutting through headings.
Similarly:
PDF splitter → respects pages.
HTML splitter → respects HTML tags.
Markdown splitter → respects headings.
JSON splitter → respects object boundaries.
Code splitter → respects functions/classes.
It preserves the document's logical structure.his is why it's called recursive—it keeps trying smaller separators until the chunk fits.

### Semantic Chunking
Semantic chunking splits text based on meaning, not on a fixed number of characters or words.
How does it work technically?
1. Split the document into sentences.
2. Convert each sentence into an embedding vector.
3. Compare neighboring sentence embeddings using cosine similarity.
4. If similarity is high, they discuss the same topic → keep them together.
5. If similarity drops below a threshold, start a new chunk.

It's chunking is more reliable for best retrievel but it is also slower and expensive since each sentence is embbeded and compared.
