"""Seeding crew — populates the ChromaDB knowledge base with stroller data."""

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from shopmind.models import StrollerList
from shopmind.tools.tools import search_web


@CrewBase
class SeederCrew:
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
