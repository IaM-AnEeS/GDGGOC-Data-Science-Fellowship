# Week 9 — Generative AI

## Overview
This directory contains the Week 9 Generative AI deliverables for a practical data science portfolio. It includes three Streamlit applications and a complementary notebook that explains core GenAI concepts, API workflows, tokenization, summarization, RAG, and a basic GAN example.

## Folder Structure
- `Final Mini Project/` — interactive math problem solver powered by LangChain and Groq Llama.
- `Q&A_Chat_bot/` — question-answer chatbot using OpenAI and LangChain.
- `RAG Document Q&A/` — retrieval augmented generation demo over PDF research papers.
- `task_15.ipynb` — learning notebook with code examples and conceptual notes.

## About `task_15.ipynb`
This notebook is an educational walkthrough designed for Week 9:
- **Foundation + Setup** — environment configuration and API key loading.
- **Gemini API examples** — using `google.generativeai` with regular and chain-of-thought prompts.
- **Tokenization Lab** — demonstrates tokenizer behavior with Hugging Face models.
- **LLM summarization** — shows text summarization using `transformers`.
- **RAG fundamentals** — introduces retrieval-augmented generation and vector search.
- **GAN fundamentals** — builds a simple PyTorch generator/discriminator pipeline.

## Prerequisites
Install dependencies from the repository root:
```bash
pip install -r requirements.txt
```

## Required Environment Variables
Create a `.env` file at the repository root with the following values:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

## Running the Notebook
Open `Week9-Gen_AI/task_15.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and execute the cells sequentially.

## Running the Streamlit Applications
From the repository root, run one of the following commands depending on the app:
```bash
streamlit run "Week9-Gen_AI/Final Mini Project/text_to_math.py"
streamlit run "Week9-Gen_AI/Q&A_Chat_bot/app.py"
streamlit run "Week9-Gen_AI/RAG Document Q&A/app.py"
```

## Recommended Workflow
1. Install dependencies and configure API keys.
2. Explore the `task_15.ipynb` notebook to understand the GenAI concepts.
3. Run the Streamlit apps to experience the interactive demos.
4. Inspect the code in each folder to learn how LangChain, embeddings, and agents are integrated.

## Notes
- `task_15.ipynb` is primarily a learning notebook and is not executed by default.
- The RAG application requires PDF files inside `Week9-Gen_AI/RAG Document Q&A/Research_papers/`.
- The Final Mini Project requires a valid Groq API key and access to the Gemma model.
- Use a Python virtual environment for dependency isolation.