from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool, ScrapeWebsiteTool, CSVSearchTool
from tools import SearchTool

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SerperDevTool()
scraper = ScrapeWebsiteTool()
file_read_tool = FileReadTool(
	file_path='resume.md',
	description='A tool to read the job description example file.'
)
resume_read = FileReadTool(
	file_path='resume.txt',
	description='A Tool to read resume file'
)
temp_read = FileReadTool(
	file_path='profile_template.json',
	description='A Tool to read profile template'
)
look_csv_tool = SearchTool(
)

csv_search_tool = CSVSearchTool(
	file_path='internships.csv',
)

class Agents():

	def parser_agent(self):
		return Agent(
			role='Resume Data Parser',
			goal='Analyze Data from Resume and fill data into json format by following profile template',
			tools=[resume_read,file_read_tool],
			backstory='Skilled in analyzing and converting data into relevant fields.',
			allow_delegation=False,
			verbose=True
		)
	
	def expert_agent(self):
		return Agent(
			role='Resume Analyzer',
			goal=' Analyze Resume and make a report for relvant jobs for it',
			tools=[],
			backstory='Expert in Application Tracking System and extracting relevant information from resume',
			verbose=True,
			allow_delegation = False
		)
	
	def find_jobs(self):
		return Agent(
			role='Job Finder ',
			goal='Find Jobs for details provided like skills, experience and projects',
			tools=[csv_search_tool],
			backstory='Expert in finding jobs for candidate',
			verbose=True,
			allow_delegation=False,
		)
	
	def query_agent(self):
		return Agent(
			role='String Generator ',
			goal='Generate String to find job id from job title',
			tools=[],
			backstory='Expert in generating string ',
			verbose=True,
			allow_delegation=False,
		)

	def writer_agent(self):
		return Agent(
			role='Resume Writer',
			goal='Analyze Report, Resume and create a tailored resume for this job posting',
			tools=[file_read_tool,web_search_tool,seper_dev_tool],
			backstory='Expert in Resume Writing and Highly Skillled in getting hired',
			verbose=True
		)
	
	def match_agent(self):
		return Agent(
			role='ATS Tool',
			goal='Analyze Report, Resume and job posting on Jeez AI internships page and give urls to apply for jobs',
			tools=[web_search_tool],
			backstory='Expert in matching resume with right job postings.',
			verbose=True
		)

	def search_agent(self):
		return Agent(
			role='Use Search Tool to search csv',
			goal='Search a CSV file  by passing string into search tool.',
			tools=[look_csv_tool],
			backstory=' ',
			verbose=True,
			allow_delegation=False
			# Additional configurations for the agent
	)
