import os
from dotenv import load_dotenv
load_dotenv()

from university_finder_crew.crew import UniversityFinderCrew

def run():
    inputs = {
        'interests':'Psychology, Anime, Maths',
        'skills': 'Maths, Data Analysis, Counselling',
        'countries': 'Germany',
        'required_degree': 'Masters',
        'financial conditions': 'Looking for a good university within tuition fees $1500-3000 per year. Also, would require a part-time job to sustain myself there.'
    }
    UniversityFinderCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()    