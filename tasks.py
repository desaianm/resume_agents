from textwrap import dedent
from crewai import Task
from tools import SearchTool

class Tasks():
		def extract_info(self, agent, profile_temp):
				return Task(
						description=dedent(f"""\
								Extracts key information such as contact details, skills, work experience, and education from resumes and fill out in {profile_temp}"""),
						expected_output=dedent("""\
								A Json File with data in sample template format """),
						agent=agent
				)
		
		def create_analysis(self,agent):
			return Task(
						description=dedent(f"""\
							Create a report of analysis for finding jobs by extracting keywords from each section in resume json file	"""),
						expected_output=dedent("""\
							 keywords from resume in string format to find jobs"""),
						agent=agent
				)

		def job_list(self, agent):
				return Task(
						description=dedent(f"""\
								Analyze the keywords about the ideal candidate have and find job titles close to it. it doesn't have to be exact match.  """),
						expected_output=dedent("""\
								List of  job titles for relevant jobs"""),
						agent=agent
				)
		
		def find_jobs(self,agent):
			return Task(
						description=dedent(f"""\
								From the given list of job title, find jobs with company names in internships csv. Keep looking untill 5 found.make sure to include company name and job title in the output file.  """),
						expected_output=dedent("""\
								List of job titles with Company Name in json format"""),
						agent=agent,
						output_file='jobs.json'
						
				)
		def create_query(self,agent):
			return Task(
						description=dedent(f"""\
								create a string with job title to find job id in internships csv and put it in search tool."""),
						expected_output=dedent("""\
								replace job_title in this {"query": "job_title"} with job title from job list json file."""),
						agent=agent
						
				)
		def find_job_id(self,agent):
			return Task(
						description=dedent(f"""\
								input 'AI Research intern' into search tool to find job id from internships csv file."""),
						expected_output=dedent("""\
								Job id of the job title from internships csv file"""),
						agent =  agent
			)
		
		
		

		
