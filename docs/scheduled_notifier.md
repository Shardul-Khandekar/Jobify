# About Jobby's scheduled_notifier.py File
This file contains code for the scheduled_notifier file in Jobby. The main purpose of this file is schedule daily runs of the main.py module so that daily job alerts are sent out to users.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/sak007/Jobby/blob/main/code/Scraper/scheduled_notifier.py)

# Code Description

This file contains contains code that schedules a call to the trigger_job(): function everyday at 10:30 AM. This runs constantly to be able to do this.

## Functions

The file contains only one function 
def trigger_job():
which runs the main.py module's run() function.

# How to run this feature?
This file is run at all times, to ensure that everyday at 10:30, the main.run() function is called and all users receive alerts.