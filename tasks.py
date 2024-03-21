from textwrap import dedent
from crewai import Task

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
							Create a report of analysis for finding jobs by extracting keywords from relevant skills, experience and projects from resume	"""),
						expected_output=dedent("""\
							relevant keywords from resume in string format to find jobs"""),
						agent=agent,
						allow_delegation = False
				)

		def job_list(self, agent):
				return Task(
						description=dedent(f"""\
								Analyze the keywords about the ideal candidate have and match with similar jobs in  internships"""),
						expected_output=dedent("""\
								List of Intern job titles for relevant jobs"""),
						agent=agent
				)
		
		def find_jobs(self,agent):
			return Task(
						description=dedent(f"""\
								From the given list of job title and find job_id and company names """),
						expected_output=dedent("""\
								List with job titles and Company Name  found in  internships csv file"""),
						agent=agent
				)
		
		

		