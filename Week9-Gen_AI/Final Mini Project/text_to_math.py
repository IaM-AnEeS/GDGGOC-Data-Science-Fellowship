import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains.base import LLMChain
from langchain.chains.llm_math.base import LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
import math
# ---------------- Streamlit App ----------------
st.set_page_config(page_title="🦜 Text to Math Problem Solver and Data Search Assistant",page_icon="🧮")
st.title("🧮 Text to Math Problem Solver using Google Gemma")

groq_api_key=st.sidebar.text_input(label="Enter your Groq API Key:", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key here")
    st.stop()

llm=ChatGroq(model_name="Gemma2-9b-It",groq_api_key=groq_api_key)

## Initializing the tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various information on the topic math"
)

## Initialize the Math Tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name= "Calculator",
    func=math_chain.run,
    description="A tool for solving math related questions. Only mathematical expressions"
)


prompt="""
You are a agent tasked for solving  user's mathematical question. Logically arrive at the solution and display it point wise
 for the question below
Question:{question}
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

### Combine all the tools in th chain
chain = LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool= Tool(
    name="Reasoning Chain",
    func=chain.run,
    description="A tool for answering logic and reasoning questions"
)

## Initialize the agents

assistant_agent = initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
    )

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {
           "role":"assistant","content":"Hi, I'm a Math chatbot who can answer all your maths questions" 
        }
    ]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    

### Function to generate the response

def generate_response(question):
    response = assistant_agent.invoke({'input':question})
    return response

## Lets start the intreraction
question =  st.text_area("Enter your question:","I have 10 bananas and 7 grapes. I eat 2 bananas and 3 grapes. How many fruits do I have left?")

if st.button("find my answer"):
    if question:
        with st.spinner("Generating response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            
            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.invoke({'input':question},callbacks=[st_cb])
            
            st.session_state.messages.append({'role':"assistant","content":response['output']})
            st.write("Response...")
            st.success(response['output'])
    
    else:
        st.warning("Please enter a question")