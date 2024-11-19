from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from crewai.project import CrewBase, agent, crew, task
from src.cache.tools.search_tool import ferramenta_busca  # Importando a ferramenta personalizada com cache

# Carregar variáveis de ambiente
load_dotenv()

@CrewBase
class Cache:
    """CacheCrew: Uma Crew configurada com cache no SerperDevTool"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['search_agent'],
            tools=[ferramenta_busca],  # Associa a ferramenta personalizada ao agente
            verbose=True,
            allow_delegation=False
        )

    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_task']
        )

    @crew
    def crew(self) -> Crew:
        """
        Criação da Crew com processo sequencial.
        """
        return Crew(
            agents=self.agents,  # Criado automaticamente pelos decorators @agent
            tasks=self.tasks,  # Criado automaticamente pelos decorators @task
            process=Process.sequential,  # Processamento em sequência
            verbose=True
        )
