"""LangGraph crew graph definition and execution."""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from shopmind.models import UserProfile, Stroller, StrollerList
from shopmind.config import MODEL
from shopmind.tools.tools import search_web, search_kb, save_kb
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class ShopMindCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher_agent"], 
            tools=[search_web]
        )

    @task
    def researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config["researcher_task"],
            output_pydantic=StrollerList
        )

    @crew
    def shopmind_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

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
    return "search_products" if state["user_profile"] and state["user_profile"].user_profile_complete() else "gather_requirements"

def should_continue_search(state: ShopMindState) -> str:
    return "build_rag_context" if len(state["search_results"]) >= 5 or state["iterations"] >= 5 else "search_products"

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