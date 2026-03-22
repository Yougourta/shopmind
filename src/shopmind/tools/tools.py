"""Agent tools: web search, vector store retrieval, and more."""

import chromadb

from openai import OpenAI, AsyncOpenAI
from langchain_core.tools import tool
from tavily import TavilyClient
from shopmind.config import TAVILY_API_KEY, TAVILY_MAX_RESULTS, CHROMA_PERSIST_DIR, CHROMA_COLLECTION_NAME, OPENAI_API_KEY

_tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
_chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
_chromadb_collection = _chroma_client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)
_openai_async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
_openai_sync_client = OpenAI(api_key=OPENAI_API_KEY)

def get_tavily_client() -> TavilyClient:
    return _tavily_client

def get_chromadb_client() -> chromadb.PersistentClient:
    return _chroma_client

def get_chromadb_collection() -> chromadb.Collection:
    return _chromadb_collection

def get_openai_async_client() -> AsyncOpenAI:
    return _openai_async_client

def get_openai_sync_client() -> OpenAI:
    return _openai_sync_client

@tool
def search_web(query: str) -> list[dict] | None:
    """Use this tool to search the web for current stroller prices and availability. 
    Use this tool when the knowledge base returns no results or when up-to-date pricing is needed."""
    results = get_tavily_client().search(
        query=query,
        max_results=TAVILY_MAX_RESULTS)
    return results["results"] or []

@tool
def search_kb(query: str) -> dict:
    """Use this tool to search for stroller recommendations in the vector database according to the user profile preferences. 
    You should also use this tool to compare price changes history after the web search"""
    results = get_chromadb_collection().query(
        query_texts=[query],
        n_results=5
    )
    return results
@tool
def save_kb(documents: list[dict]) -> None:
    """Use this tool to save stroller recommendations found on the web to the vector database. Also use this tool to update stroller information gathered on the web."""
    get_chromadb_collection().add(
        ids=[doc["id"] for doc in documents],
        documents=[doc["content"] for doc in documents],
        metadatas=[{k: v for k, v in doc.items() if k != "content"} for doc in documents]
    )