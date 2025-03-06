# Imports
from crewai import Crew
from ai_agents_crewai_template.agents.agents_definitions import CustomAgents
from ai_agents_crewai_template.tasks.tasks_definitions import CustomTasks

## Initalize
custom_agents = CustomAgents()
custom_tasks = CustomTasks()
custom_agent_1 = custom_agents.agent_1_name()


# Define your crews
class CustomCrews:

    # Crew definitions
    def crew_1_name(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        # Define your custom crew here

        # Variables specific to this crew here here
        var1 = "Global warming"
        # Capture inputs here if required

        # Return an instance of crew
        return Crew(
            agents=[custom_agent_1],
            tasks=[custom_tasks.task_1_name(custom_agent_1, var1)],
            verbose=True,
        )
