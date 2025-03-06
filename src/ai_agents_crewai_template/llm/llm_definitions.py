# Imports
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

# Define LLMs
class LLMDefinitions:

      def __init__(self):
        
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")