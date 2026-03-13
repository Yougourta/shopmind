"""Agent tools: web search, vector store retrieval, and more."""

from langchain_core.tools import tool
from tavily import TavilyClient
from config import TAVILY_API_KEY, TAVILY_MAX_RESULTS

@tool
def search_web(query: str) -> list[dict] | None:
    """Use this tool to search the web for current stroller prices and availability. 
    Use this tool when the knowledge base returns no results or when up-to-date pricing is needed."""
    client = TavilyClient(api_key=TAVILY_API_KEY)
    results = client.search(
        query=query,
        max_results=TAVILY_MAX_RESULTS)
    return results["results"] or []

@tool
def search_kb(query: str) -> str:
    """Use this tool to search for stroller recommendations in the vector database according to the user profile preferences. 
    You should also use this tool to compare price changes history after the web search"""
    pass

@tool
def save_kb(document: list[dict]) -> None:
    """Use this tool to save stroller recommendations found on the web to the vector database. Also use this tool to update stroller information gathered on the web."""
    pass



    