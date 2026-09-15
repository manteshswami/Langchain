from dotenv import load_dotenv
load_dotenv()
import os

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import All_TOOLS

MODEL = os.getenv("MODEL")
def get_agent():
    
    return create_agent(
        model=ChatGroq(model=MODEL),
        tools=All_TOOLS,
        
    )