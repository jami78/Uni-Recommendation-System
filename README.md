# Uni-Recommendation-System

A CrewAI system designed to help individuals find university programs that match their career goals, skills, and interests. The system identifies high-paying global job opportunities, matches them with the user's profile, and recommends university programs that prepare the individual for those roles. Additionally, it integrates financial analysis, scholarship information, and personalized recommendations to help users make informed decisions.

## System Architecture

The CrewAI system is built using multiple agents, each focusing on a unique part of the recommendation process:

Job Identifier Agent: Searches for high-paying jobs worldwide.
Skills Matching Agent: Matches the identified top-paying jobs with user's profile to identify suitable jobs for the user.
University Finder Agent: Recommends educational programs that help users achieve their career goals.
Scholarship Agent: Finds and assesses relevant scholarship opportunities.
Financial Analysis Agent: Evaluates budget, living expenses, and part-time job possibilities based on the user's financial data.
Profile Enhancement Agent: Provides suggestions to improve the user's profile for better acceptance and scholarship opportunities.
Personalized Recommendation Agent: Provides individual specific personalized recommendations.

## Setup Instructions
## Requirements
Download groq, crewai, langachain and crewai_tools using pip.

### Clone the Repository:
git clone https://github.com/jami78/Uni-Recommendation-System/

cd university_finder_crew

### Environment Setup:

Create a .env file in the root directory.

API Keys: You will need API keys for Groq and SerperDev.

In the .env file, add the following:
**GROQ_API_KEY=your_groq_api_key**

**SERPER_API_KEY=your_serper_api_key**

### Resume File:

Place the resume file (for skills assessment) in the specified directories.

Make sure the paths in src\university_finder_crew\crew.py match the locations of the file.

## Project Structure

src/university_finder_crew/config/: Configuration files for defining agents and tasks.

src/university_finder_crew/tools/: Custom tools for data processing and API calls.

src/university_finder_crew/crew.py: Main CrewAI system file that sets up agents and tasks.

src/university_finder_crew/main.py: Backend execution file to run the CrewAI system.

readme.md: Project documentation.

## Important Note

This system relies on Groq and SerperDev APIs for functionality. Make sure you have valid API keys from these services and have added them to your environment variables in .env.

