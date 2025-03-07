# Imports
from crewai import Agent
from textwrap import dedent
from ai_agents_crewai_template.llm.llm_definitions import LLMDefinitions
from ai_agents_crewai_template.tools.tools_definitions import SerperDevTool, tool_1_name

# Initialise
llm_definitions = LLMDefinitions()
serper_dev_tool = SerperDevTool()


# Define custom agents
class CustomAgents:

    # Agent defintion
    def agent_1_name(self):
        return Agent(
            role="you are a researcher",
            backstory=dedent(
                f"""You have some good expereince in researching topics and fetcing summarized information"""
            ),
            goal=dedent(
                f"""Get 100 words of summarized infromation on the soecified topic"""
            ),
            tools=[serper_dev_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )
