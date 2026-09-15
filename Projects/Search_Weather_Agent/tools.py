from langchain_nimble import NimbleSearchTool
from langchain.tools import tool


search_tool= NimbleSearchTool(
    k=5,
    deep_search=True,
    parsing_type="markdown"
)

@tool
def google_search(query: str):
    """
    Search Anything on Google for Real time Information.
    args:
        query: user search for google search
        
    return: result from google search
    """
    res = search_tool.invoke(query)
    return res

@tool
def weather_tool(city:str):
    """
    Args:
        city (str): city name for weather detection
       
    retuen: weather data from the api respoance
    """
    return f"The Current Temp in {city} is 23.C"

All_TOOLS = [google_search, weather_tool]