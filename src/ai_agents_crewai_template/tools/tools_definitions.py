from crewai_tools import SerperDevTool
from crewai.tools import tool


@tool("Market analysis tool")
def tool_1_name(question: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return "Result from your custom tool"
