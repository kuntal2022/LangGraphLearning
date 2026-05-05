import streamlit as st 
st.header("AI-Agent-App")
user_input = st.text_input("Ask a Question")
user_id = st.text_input("Enter User ID")

from langchain.agents import create_agent
import os
from dotenv import load_dotenv
load_dotenv()

from langgraph.checkpoint.memory import InMemorySaver
from langchain_community.tools import TavilySearchResults, DuckDuckGoSearchRun


config={'configurable':{'thread_id':user_id}}
if st.button("Ask"):
    agent=create_agent(
        model = 'gpt-4o-mini',
        checkpointer=InMemorySaver(),
        tools=[TavilySearchResults(max_results=3), DuckDuckGoSearchRun()]
        )

    
    response=agent.invoke({'messages':user_input},config=config)
    st.write(response['messages'][-1].content)