import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import time

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

groq_api_key = os.getenv("GROQ_API_KEY")

# Base directory — always points to the folder where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESEARCH_PAPERS_PATH = os.path.join(BASE_DIR, "Research_papers")

llm = ChatGroq(model_name="llama3-8b-8192", groq_api_key=groq_api_key)

prompt = ChatPromptTemplate.from_template("""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question.
<context>
{context}
</context>
Question: {input}
""")

def create_vector_embeddings():
    if "vector_store" not in st.session_state:
        with st.spinner("Loading and embedding documents..."):

            # Debug: show exact path being searched
            st.info(f"📂 Looking for PDFs in: {RESEARCH_PAPERS_PATH}")

            if not os.path.exists(RESEARCH_PAPERS_PATH):
                st.error(f"❌ Folder does not exist: {RESEARCH_PAPERS_PATH}")
                return

            pdf_files = [f for f in os.listdir(RESEARCH_PAPERS_PATH) if f.endswith(".pdf")]
            if not pdf_files:
                st.error(f"❌ No PDF files found in: {RESEARCH_PAPERS_PATH}")
                st.write("Files found:", os.listdir(RESEARCH_PAPERS_PATH))
                return

            st.write(f"📄 Found {len(pdf_files)} PDF(s): {pdf_files}")

            st.session_state.embeddings = OpenAIEmbeddings()
            st.session_state.loader = PyPDFDirectoryLoader(RESEARCH_PAPERS_PATH)
            st.session_state.docs = st.session_state.loader.load()

            if not st.session_state.docs:
                st.error("❌ PDFs found but could not be loaded. They may be scanned/image-based.")
                return

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            split_docs = text_splitter.split_documents(st.session_state.docs)

            if not split_docs:
                st.error("❌ Documents loaded but splitting produced no chunks.")
                return

            st.session_state.vector_store = FAISS.from_documents(split_docs, st.session_state.embeddings)
            st.session_state.split_docs = split_docs

st.title("RAG Q&A over Research Papers")
user_prompt = st.text_input("Enter your question here:")

if st.button("Document Embedding"):
    create_vector_embeddings()
    if "vector_store" in st.session_state:
        st.success(f"✅ Vector database ready — {len(st.session_state.split_docs)} chunks indexed.")

if user_prompt:
    if "vector_store" not in st.session_state:
        st.warning("⚠️ Please embed documents first.")
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

        with st.expander("📄 Document similarity search"):
            for i, doc in enumerate(response.get('context', [])):
                st.markdown(f"**Document {i+1}:**")
                st.write(doc.page_content)
                st.write("📁 Source:", doc.metadata.get('source', 'Unknown'))
                st.write("---")