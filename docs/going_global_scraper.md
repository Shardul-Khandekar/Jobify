# About Jobby's going_global_scraper.py File
This file contains code for the global scraper in Jobby. The main function of this file is scrape the job board website, [https://www.goinglobal.com/](https://www.goinglobal.com/).

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/Jobby/blob/main/code/Scraper/going_global_scraper.py)

# Code Description
## Functions

The file contains only one function def get_jobs(role, location, no_of_jobs_to_retrieve, all_skills, country=""): , which uses the BeautifulSoup library in Python to scrape job data from the goingglobal website, and then proceeds to retrieve the following details for all jobs found:

1. Job Position
2. Company Name
3. Job URL
4. Job skills matching with all_skills

# How to run this feature?
This file is run when the user selects the going global scraper in web app. The file is run to scrape jobs based on the user location, and then it matches the job skills with the user's skills and returns the matching skills for each job position. 