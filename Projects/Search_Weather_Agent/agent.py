from dotenv import load_dotenv
load_dotenv()
import os

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import All_TOOLS
from langgraph.checkpoint.memory import InMemorySaver

MODEL = os.getenv("MODEL")
def get_agent():
    "Get Agent with google search and weather search abilities"
    return create_agent(
        model=ChatGroq(model=MODEL),
        tools=All_TOOLS,
        system_prompt=(
            "Ypu are a research assistent with google search and weather tools.\n"
            "Use 'google_search' for quick search on google"
            "for deep search that may take several minutes."
            "if user is looking for weather detatils like temprature, humidity or any other detail then call the weather tool to get the live real time weather data."
        ),
        checkpointer=InMemorySaver()
    )
    
    
# agent = get_agent()
# while True:
#     query=input("User: ")
#     if query == "exit":
#         break
    
#     res = agent.invoke(
#         {"messages":[
#             {"role":"user",
#              "content":query
#             }
#         ]}
#     )
    
#     ans = res["messages"][-1].content
#     print("AI: ", ans)
    