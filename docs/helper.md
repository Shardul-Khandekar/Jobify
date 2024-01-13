# About Jobby's helper.py File
This file contains code for the helper.py module in Jobby. The main function of this file is to simplify the execution of common tasks from scrapers and the main functions such as connecting to the database, getting skills for users, getting all skills etc.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/Jobby/blob/main/code/Scraper/helper.py)

# Code Description
## Functions

1. def db_connect():
Connects to the database with properties read from the parameters.json file. Return the connection object for other functions/modules to use and make changes.

2. def get_all_skills():
Uses db_connect to get a connections and reads all skills in the skill master table in the database, which are returned together in a list.

3. def extract_skills(desc, skills):
Takes 2 arguments - desc, which is a job posting description and skills, which are a list of skills to look for in said job posting. It parses desc and checks if any or some or all of the skills are there, and returns the ones that are in both.

4. def matching_skills(skills1, skills2):
Takes 2 arguments - skills1 and skills2, which are lists containing skills, and returns the matching skills between both.

5. def match_percentage(user_skills, job_skills):
Takes 2 arguments, user_skills which contains the skills of a user using Jobby, and the skills in the job description, and computes a percentage of matching skills.

6. def print_matching_skills(skills1, skills2):
Takes 2 arguments, skills1 and skills2, which are lists containing skills, and prints the matching skills between both.

7. def get_user_skills_map():
Connects to the database and gets the userdata for all users - email and skills and returns a map containing these.

8. def filter_jobs(user_jobs, user_skills):
Takes 2 arguments - user_jobs, and user_skills. user jobs is the list of matching jobs and user skills is the list of skills of the user. It returns only those jobs which satisfy a certain percentage criteria called MATCH_THRESHOLD. 


# How to run this feature?
This file is throughout the processing of Jobby as it performs myriad functions which all require the different functionalities it offers.