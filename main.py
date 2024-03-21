import os
from crewai import Crew
from tasks import Tasks
from agents import Agents
from dotenv import load_dotenv
import pandas as pd
from langchain_community.document_loaders import CSVLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
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

# Define Tasks for each agent
review = tasks.extract_info(parser_agent,resume_temp)
#report = tasks.create_analysis(expert_agent)
job_list = tasks.job_list(find_agent)
jobs_find = tasks.find_jobs(find_agent)

# Instantiate the crew with a sequential process
crew = Crew(
        agents=[parser_agent,find_agent],
        tasks=[
            review, job_list, jobs_find
        ]
)

# Kick off the process
result = crew.kickoff()

print(result)