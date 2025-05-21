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

# Advanced RAG Techniques Used
- Instead of just using the original question to search the database, we first ask the language model (LLM) to give an initial answer. Then, we combine the original question and this first answer to search the database again. This helps us find better and more relevant information, which the LLM uses to give a more accurate final answer.

- We also ask the LLM to create multiple new versions of the original question. These new questions cover different ways to ask or understand the same thing. We use all these new questions to search the database, which helps us find more useful pieces of information. We gather all these pieces and give them to the LLM so it can create a richer and more complete answer.

## Ranking
- After collecting many pieces of information from the database, we don’t just send them all to the LLM. Instead, we rank them based on how relevant they are to the original question. We pick the best ones and only send those to the LLM. This way, the answer is based on the most important and useful information, making it clearer and more accurate.


