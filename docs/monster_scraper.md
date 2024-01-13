# About Jobby's monster_scraper.py File
This file contains code for the monster scraper file in Jobby. The main function of this file is scrape the job board website, monster [https://www.monster.com/](https://www.monster.com/).

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/Jobby/blob/main/code/Scraper/monster_scraper.py)

# Code Description
## Functions

The file contains only one function 
def get_jobs(role, location, no_of_jobs_to_retrieve, all_skills):
, which uses the BeautifulSoup library in Python to scrape job data from the monster.com website, and then proceeds to retrieve the following details for all jobs found:

1. Job Position
2. Company Name
3. Job URL
4. Job skills matching with all_skills

# How to run this feature?
This file is run when the user selects the monster scraper in web app. The file is run to scrape jobs based on the user location, and then it matches the job skills with the user's skills and returns the matching skills for each job position. 