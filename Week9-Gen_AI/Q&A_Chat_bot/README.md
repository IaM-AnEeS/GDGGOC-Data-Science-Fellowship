# Q&A Chat Bot

## Overview
This folder contains a polished Streamlit-based Q&A chatbot built using LangChain and OpenAI. It is designed to provide a clean user experience for asking natural language questions and receiving concise, relevant answers.

## What This App Does
- Presents a user-friendly chat interface in Streamlit.
- Uses a reusable LangChain prompt template to structure questions.
- Sends requests to OpenAI through the `ChatOpenAI` client.
- Uses `StrOutputParser` to ensure clean text output.
- Supports model selection, temperature control, and dynamic user input.

## Files
- `app.py` — main Streamlit application.

## Architecture
1. Reads environment variables and loads `.env` values.
2. Configures LangChain with a chat prompt template.
3. Creates a pipeline that connects the prompt, the OpenAI model, and the output parser.
4. Displays a sidebar for the API key, model selection, temperature, and token controls.
5. Processes user questions and renders the answers in the app.

## Prerequisites
Install dependencies from the repository root:
```bash
pip install -r requirements.txt
```

## Environment Setup
Create a `.env` file in the repository root with the following keys:
```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

## Run the Chat Bot
From the repository root, execute:
```bash
streamlit run "Week9-Gen_AI/Q&A_Chat_bot/app.py"
```

## How to Use
1. Start the app and open the browser URL that Streamlit provides.
2. Enter your OpenAI API key in the sidebar.
3. Choose between supported OpenAI models.
4. Type a question in the text input and submit.
5. Read the chatbot’s response instantly.

## Best Practices
- Use short, specific questions for clearer answers.
- Try different models and temperature settings to compare behavior.
- Keep the OpenAI API key private and do not commit it to GitHub.

## Notes
- The app is a demonstration of LangChain’s pipeline pattern with OpenAI.
- It uses the `langchain_openai` package and requires valid credentials.
- For production use, add error handling and API key validation.