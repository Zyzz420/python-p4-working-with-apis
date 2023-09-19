import requests
import json

class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        try:
            response = requests.get(URL)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error occurred during the API request: {e}")
            return None

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs() or "[]") 
        for program in programs:
            programs_list.append(program.get("agency"))  

        return programs_list

programs = GetPrograms()
programs_schools = programs.program_school()

if programs_schools is not None:
    for school in set(programs_schools):
        print(school)