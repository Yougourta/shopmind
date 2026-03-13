"""LangGraph agent graph definition and execution."""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from src.models import UserProfile


class ShopMindState(TypedDict):
    messages: list[dict]        # Conversation history
    user_profile: UserProfile | None
    search_results: list[dict]  # Tavily and ChromaDB results
    recommendations: list[dict] # Top 3 selected
    iterations: int             # Number of searches performed
    error: str | None


# --- Node functions ---

def gather_requirements(state: ShopMindState) -> ShopMindState:
    pass


def search_products(state: ShopMindState) -> ShopMindState:
    pass


def build_rag_context(state: ShopMindState) -> ShopMindState:
    pass


def generate_recommendations(state: ShopMindState) -> ShopMindState:
    pass


def format_response(state: ShopMindState) -> ShopMindState:
    pass


# --- Routing functions ---

def should_continue_profiling(state: ShopMindState) -> str:
    pass


def should_continue_search(state: ShopMindState) -> str:
    pass


# --- Graph builder ---

def build_graph() -> StateGraph:
    builder = StateGraph(ShopMindState)

    builder.add_node("gather_requirements", gather_requirements)
    builder.add_node("search_products", search_products)
    builder.add_node("build_rag_context", build_rag_context)
    builder.add_node("generate_recommendations", generate_recommendations)
    builder.add_node("format_response", format_response)

    builder.add_edge(START, "gather_requirements")

    builder.add_conditional_edges(
        "gather_requirements",
        should_continue_profiling,
        {"gather_requirements": "gather_requirements", "search_products": "search_products"},
    )

    builder.add_conditional_edges(
        "search_products",
        should_continue_search,
        {"search_products": "search_products", "build_rag_context": "build_rag_context"},
    )

    builder.add_edge("build_rag_context", "generate_recommendations")
    builder.add_edge("generate_recommendations", "format_response")
    builder.add_edge("format_response", END)

    return builder.compile()

# --- Entry point ---

async def run_agent(state: ShopMindState) -> dict:
    graph = build_graph()
    return await graph.ainvoke(state)
