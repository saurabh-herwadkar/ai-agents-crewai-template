# Imports
from crewai import Task
from textwrap import dedent
from ai_agents_crewai_template.agents.agents_definitions import CustomAgents
# Initalize
custom_agents = CustomAgents()


# Define your tasks here
class CustomTasks:
    
    # Task definition
    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            Do something as part of task 1
                
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
            And also this variable: {var2}
        """
            ),
            expected_output="The expected output of the task",
            agent=custom_agents.agent_1_name,
        )