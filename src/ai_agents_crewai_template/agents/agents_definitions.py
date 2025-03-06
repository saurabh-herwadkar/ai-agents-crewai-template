# Imports
from crewai import Agent
from textwrap import dedent
from ai_agents_crewai_template.llm.llm_definitions import LLMDefinitions

# Initialise
llm_definitions = LLMDefinitions()


# Define custom agents
class CustomAgents:

    # Agent defintion
    def agent_1_name(self):
        return Agent(
            role="Define agent 1 role here",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""Define agent 1 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )
