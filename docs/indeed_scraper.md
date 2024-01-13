# About Jobby's indeed_scraper.py File
This file contains code for the indeed scraper file in Jobby. The main function of this file is scrape the job board website, indeed [https://www.indeed.com/](https://www.indeed.com/).

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/Jobby/blob/main/code/Scraper/indeed_scraper.py)

# Code Description
## Functions

The file contains only one function 
def get_jobs(role, location, no_jobs, allskills):
, which uses the BeautifulSoup library in Python to scrape job data from the indeed.com website, and then proceeds to retrieve the following details for all jobs found:

1. Job Position
2. Company Name
3. Job URL
4. Job skills matching with all_skills

# How to run this feature?
This file is run when the user selects the indeed scraper in web app. The file is run to scrape jobs based on the user location, and then it matches the job skills with the user's skills and returns the matching skills for each job position. 