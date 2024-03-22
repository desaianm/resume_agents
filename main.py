import os
from crewai import Crew
from tasks import Tasks
from agents import Agents
from dotenv import load_dotenv
import pandas as pd
import json

#os.environ['KMP_DUPLICATE_LIB_OK']='True'
load_dotenv()

tasks = Tasks()
agents = Agents()

with open('profile_template.json', 'r') as file:
    resume_temp = json.load(file)


# Create Agents
parser_agent = agents.parser_agent()
expert_agent = agents.expert_agent()
writer_agent = agents.writer_agent()
find_agent = agents.find_jobs()
query_agent = agents.query_agent()
search_agent = agents.search_agent()

# Define Tasks for each agent
review = tasks.extract_info(parser_agent,resume_temp)
report = tasks.create_analysis(expert_agent)
job_list = tasks.job_list(find_agent)
jobs_find = tasks.find_jobs(find_agent)
create_query = tasks.create_query(query_agent)
find_job_id = tasks.find_job_id(search_agent)

# create query and find_job_id
# Instantiate the crew with a sequential process
crew = Crew(
        agents=[parser_agent,find_agent, expert_agent],
        tasks=[
            review,
            report,
            job_list,
            jobs_find
        ]
)

# Kick off the process
result = crew.kickoff()

print(result)
