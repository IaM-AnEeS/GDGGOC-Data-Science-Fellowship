import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load env
load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with LangSmith"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions clearly."),
        ("user", "Question: {question}")
    ]
)


def generate_response(question, api_key, model_name, temperature, max_tokens):
    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})


st.title("🤖 Q&A Chatbot with OpenAI + LangSmith")

st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

model = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o", "gpt-4-turbo", "gpt-4"]
)

temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, 0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens", 50, 500, 150
)


st.write("Ask anything 👇")

user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    else:
        with st.spinner("Thinking..."):
            response = generate_response(
                user_input,
                api_key,
                model,
                temperature,
                max_tokens
            )
            st.success(response)
else:
    st.info("Enter a question to get started.")