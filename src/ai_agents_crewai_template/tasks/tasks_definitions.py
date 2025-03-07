# Imports
from crewai import Task
from textwrap import dedent


# Define your tasks here
class CustomTasks:

    # Task definition
    def task_1_name(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Get some information on the topic. 
            Information should not contain any aggressive or inflammatory content
            Do not use hyperbole or exaggeration
            onlky use the tools supplied to you and do not use any other tools
    
            Use this topic: {var1}
            
        """
            ),
            expected_output="Share 200 words on the specified topic as an essay text also share the secret code",
            agent=agent,
        )
