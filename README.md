# RAG(Retrieval-Augmented Generation)


# Document-Based Question Answering with Ollama & ChromaDB
## Overview
This project enables you to ask questions and get precise answers based on your own document files. It works by:

- Loading your text files from a folder.
- Splitting documents into smaller chunks.
- Generating vector embeddings for each chunk using the free Ollama model.
- Storing these embeddings efficiently in ChromaDB (a free vector database).
- Querying the database to find relevant document chunks matching your question.
- Using Ollama Llama3.1 chat model to generate a short, precise answer based on retrieved context.

# Models Used
- Embedding model: __mxbai-embed-large:latest__ (pulled from Ollama for generating embeddings)

- Chat/Response model: __llama3.1__ (pulled from Ollama for generating answers)

Make sure these models are pulled and available locally in your Ollama environment.
