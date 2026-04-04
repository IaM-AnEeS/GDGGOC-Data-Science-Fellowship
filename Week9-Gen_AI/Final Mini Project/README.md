# Final Mini Project — Text-to-Math Problem Solver

## Project Summary
This folder contains a polished Streamlit application that transforms natural language math questions into structured reasoning and computation. The project demonstrates how to combine an LLM with a math calculator tool, external knowledge retrieval, and a task-routing agent for accurate and explainable answers.

## Key Features
- Interactive Streamlit user interface for chat-style math solving.
- Natural language question parsing with `ChatGroq` and Google Gemma.
- Mathematical reasoning through `LLMMathChain`.
- Supplementary knowledge lookup using Wikipedia.
- Agent-based tool selection to route questions to the best available capability.
- Persistent chat history stored in Streamlit session state.

## File Structure
- `text_to_math.py` — main application script.

## How the App Works
1. Streamlit renders a clean UI and prompts the user for a Groq API key.
2. The app initializes `ChatGroq` with the selected Gemma model.
3. A Wikipedia tool is created for context lookup when additional knowledge is needed.
4. `LLMMathChain` is built for calculation and symbolic math logic.
5. A reasoning chain is registered to produce structured, step-by-step explanations.
6. The LangChain agent decides whether to use Wikipedia, the calculator, or reasoning based on the user query.
7. Output is displayed in the Streamlit chat interface, and the interaction history is preserved.

## Installation
Install dependencies from the repository root:
```bash
pip install -r requirements.txt
```

## Environment Setup
Create a `.env` file in the repository root (optional) or enter your Groq API key in the app sidebar.

Required environment variable:
```env
GROQ_API_KEY=your_groq_api_key
```

## Run Locally
From the repository root, start the app with:
```bash
streamlit run "Week9-Gen_AI/Final Mini Project/text_to_math.py"
```

Then open the local Streamlit URL in your browser, enter the API key, and submit a math question.

## Recommended Usage
- Use clear arithmetic or word math problems.
- For complex reasoning, allow the model to explain answers step-by-step.
- If the app does not respond, verify the API key and model selection.

## Notes
- The project depends on `langchain`, `langchain-groq`, `langchain-community`, `streamlit`, and `WikipediaAPIWrapper`.
- Ensure your Groq API key has access to the `Gemma2-9b-It` model.
- This app is designed to be shareable on GitHub and easy to run on any laptop with Python installed.