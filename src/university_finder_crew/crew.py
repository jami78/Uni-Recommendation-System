from datetime import datetime
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool




scrape_tool= ScrapeWebsiteTool()
search_tool= SerperDevTool()
read_resume = FileReadTool(file_path='/teamspace/studios/this_studio/src/university_finder_crew/resume.md')

@CrewBase
class UniversityFinderCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0.1, model_name="llama3-70b-8192")
    @agent
    def job_identifier_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['job_identifier_agent'],
            llm = self.groq_llm,
            tools= [search_tool, scrape_tool],
        )

    @agent
    def skills_matcher_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['skills_matcher_agent'],
            llm = self.groq_llm,
            tools= [read_resume]
        )
    
    @agent
    def university_program_matcher(self) -> Agent:
        return Agent(
            config = self.agents_config['university_program_matcher'],
            llm = self.groq_llm,
            tools= [search_tool, scrape_tool]
        )

    @agent
    def scholarship_finder(self) -> Agent:
        return Agent(config=self.agents_config['scholarship_finder'],
                     llm= self.groq_llm,
                     tools= [search_tool, scrape_tool]
        )

    @agent
    def financial_evaluator(self) -> Agent:
        return Agent(config=self.agents_config['financial_evaluator'],
                     llm= self.groq_llm,
                     tools= [search_tool, scrape_tool]
        )

    @agent
    def profile_improvement_advisor(self) -> Agent:
        return Agent(config=self.agents_config['profile_improvement_advisor'],
                     llm= self.groq_llm,
                     tools= [read_resume]
        )

    @agent
    def personalized_recommendation_agent(self) -> Agent:
        return Agent(
            config= self.agents_config['personalized_recommendation_agent'],
            llm=self.groq_llm
        )



    @task
    def job_identification_task(self) -> Task:
        return Task(
            config = self.tasks_config['job_identification_task'],
            agent = self.job_identifier_agent()
        )

    @task
    def skills_matching_task(self) -> Task:
        return Task(
            config = self.tasks_config['skills_matching_task'],
            agent = self.skills_matcher_agent()
        )
    
    @task
    def program_matching_task(self) -> Task:
        return Task(
            config = self.tasks_config['program_matching_task'],
            agent = self.university_program_matcher()
        )
    @task
    def find_scholarships_task(self) -> Task:
        return Task(config=self.tasks_config['find_scholarships_task'], agent=self.scholarship_finder())

    @task
    def evaluate_financials_task(self) -> Task:
        return Task(config=self.tasks_config['evaluate_financials_task'], agent=self.scholarship_finder())

    @task
    def improve_profile_task(self) -> Task:
        return Task(config=self.tasks_config['improve_profile_task'], agent=self.profile_improvement_advisor())

    @task
    def personalized_recommendation_task(self) -> Task:
        return Task(
            config = self.tasks_config['personalized_recommendation_task'],
            agent = self.personalized_recommendation_agent()
        )


    @crew
    def crew(self) -> Crew:
        """Creates the UniversityFinder crew"""
        return Crew(
            agents = [self.job_identifier_agent(), self.skills_matcher_agent(),self.university_program_matcher(),self.scholarship_finder(), self.financial_evaluator(),self.profile_improvement_advisor(), self.personalized_recommendation_agent()],
            tasks = [self.job_identification_task(), self.skills_matching_task(), self.program_matching_task(), self.find_scholarships_task(), self.evaluate_financials_task(), self.improve_profile_task(), self.personalized_recommendation_task(),],
            process = Process.sequential,
            verbose = 2
        )
