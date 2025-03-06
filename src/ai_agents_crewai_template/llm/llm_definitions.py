# Imports
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
import os


# Define LLMs
class LLMDefinitions:

    def __init__(self):

        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
