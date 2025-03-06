# Imports
from  ai_agents_crewai_template.crews.crews_definitions import CustomCrews
# Initalize
custom_crew = CustomCrews()

# The main program to run
# Your crews related code will come here
def run():
    
    print("----------------------")
    crew_1 = custom_crew.crew_1_name
    result = crew_1.kickoff()
    return result
    