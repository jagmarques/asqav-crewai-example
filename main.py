"""
asqav + CrewAI - Governance for multi-agent teams.

Run: python main.py
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from asqav.integrations.crewai import AsqavCrewHook

load_dotenv()

# Initialize the asqav hook
hook = AsqavCrewHook()

# Define two agents with different roles
researcher = Agent(
    role="Researcher",
    goal="Find accurate, recent information on the given topic",
    backstory="You are a thorough researcher who finds reliable sources.",
    verbose=True,
)

writer = Agent(
    role="Writer",
    goal="Turn research into clear, concise summaries",
    backstory="You are a technical writer who explains complex topics simply.",
    verbose=True,
)

# Define tasks
research_task = Task(
    description="Research the current state of AI governance frameworks worldwide. Focus on the EU AI Act and recent US executive orders.",
    expected_output="A list of key frameworks with brief descriptions.",
    agent=researcher,
)

summary_task = Task(
    description="Take the research and write a 3-paragraph summary suitable for a developer audience.",
    expected_output="A clear, jargon-free summary of AI governance frameworks.",
    agent=writer,
)

# Create and run the crew with asqav governance
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, summary_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff(hooks=[hook])

print("
--- Result ---")
print(result)

# Print audit summary
print("
--- Audit Trail ---")
hook.print_summary()
