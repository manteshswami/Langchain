from langchain_nimble import NimbleSearchTool
from langchain.tools import tool
import os
import requests

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
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("WEATHER_API_KEY")}"
    res = requests.get(API_URL)
    if res.status_code == 200:
        return res.json()
    return "Unable to find details for the {city}"

All_TOOLS = [google_search, weather_tool]