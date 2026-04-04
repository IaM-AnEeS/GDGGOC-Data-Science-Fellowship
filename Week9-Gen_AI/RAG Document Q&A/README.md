# RAG Document Q&A

## Overview
This folder contains a Retrieval-Augmented Generation (RAG) demo built with Streamlit and LangChain. The application indexes PDF research papers, builds a semantic vector store, and answers user queries using retrieval-based context plus LLM generation.

## What This App Delivers
- Document ingestion from PDF files.
- Text chunking for efficient retrieval.
- FAISS-based vector search for semantic similarity.
- OpenAI embeddings for text encoding.
- A clean Streamlit interface for embedding documents and asking questions.
- Transparent source display showing which documents informed each answer.

## Files
- `app.py` — primary Streamlit app.
- `Research_papers/` — folder containing PDF files to index.

## Architecture
1. `PyPDFDirectoryLoader` reads all PDF files from `Research_papers/`.
2. `RecursiveCharacterTextSplitter` breaks long documents into retrievable chunks.
3. `OpenAIEmbeddings` encodes text chunks into vectors.
4. `FAISS.from_documents()` builds the semantic search index.
5. LangChain retrieval and generation chains are assembled with `ChatGroq`.
6. User questions are answered using retrieved context and the LLM.

## Prerequisites
Install dependencies from the repository root:
```bash
pip install -r requirements.txt
```

## Environment Setup
Create a `.env` file in the repository root with:
```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Run the App
From the repository root, launch:
```bash
streamlit run "Week9-Gen_AI/RAG Document Q&A/app.py"
```

## Usage Instructions
1. Click **Document Embedding** to load and index your PDFs.
2. Wait until the vector database is ready.
3. Enter a question in the input field.
4. Review the answer and optionally inspect the source document excerpts.

## Best Practices
- Store your PDFs in the `Research_papers/` directory.
- Use concise, research-focused questions for the best results.
- If no answer appears, ensure documents are correctly loaded and the embeddings step completed.

## Notes
- This app requires both Groq and OpenAI credentials.
- The retrieval chain returns both the answer and context sources for auditability.
- For production use, add persistence to the vector store and support incremental document updates.