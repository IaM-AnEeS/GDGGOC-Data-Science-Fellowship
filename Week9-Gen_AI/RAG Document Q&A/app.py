import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
# from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

groq_api_key = os.getenv("GROQ_API_KEY")

# Load LLM
llm = ChatGroq(model_name="Llama3-8b-8192", groq_api_key=groq_api_key)

# Correct prompt usage: use `from_template()` or `from_messages()` with message tuples
prompt = ChatPromptTemplate.from_template("""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question.
<context>
{context}
</context>
Question: {input}
""")

# Vector embedding creation
def create_vector_embeddings():
    if "vector_store" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("Research_papers")
        st.session_state.docs = st.session_state.loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(st.session_state.docs)
        st.session_state.vector_store = FAISS.from_documents(split_docs, st.session_state.embeddings)
        st.session_state.split_docs = split_docs

# UI
st.title("RAG Q&A over Research Papers")
user_prompt = st.text_input("Enter your question here:")

if st.button("Document Embedding"):
    create_vector_embeddings()
    st.success("✅ Vector database is ready.")

if user_prompt:
    if "vector_store" not in st.session_state:
        st.warning("Please embed documents first.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vector_store.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        start = time.process_time()
        response = retrieval_chain.invoke({'input': user_prompt})
        duration = time.process_time() - start
        st.write(f"⏱️ Response Time: {duration:.2f} seconds")

        st.markdown("### Answer:")
        st.write(response['answer'])

        # Show source documents
        with st.expander("📄 Document similarity search"):
            for i, doc in enumerate(response.get('context', [])):
                st.markdown(f"**Document {i+1}:**")
                st.write(doc.page_content)
                st.write("📁 Source:", doc.metadata.get('source', 'Unknown'))
                st.write("---")
