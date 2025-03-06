# Imports
from dotenv import load_dotenv

load_dotenv()

import os
import logging

logging.info("----------------------")
logging.info(os.environ.get("OPENAI_API_KEY"))

from ai_agents_crewai_template.crews.crews_definitions import CustomCrews
import logging

# Initalize
custom_crew = CustomCrews()


# The main program to run
# Your crews related code will come here
def run():

    logging.info("----------------------")
    crew_1 = custom_crew.crew_1_name()
    result = crew_1.kickoff()
    return result
