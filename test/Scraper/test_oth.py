import requests

from importlib.machinery import SourceFileLoader
goinglobal_scraper = SourceFileLoader('going_global_scraper', 'code/Scraper/going_global_scraper.py').load_module()


def test_get_job_goin_global(mocker):
    final_result = goinglobal_scraper.get_jobs("Programmer", "", 5, ["Programmer", "Analytic", "Experience"])
    assert final_result is not None


def test_goin_global_scraper_nonworking(mocker):
    mocker.patch.object(goinglobal_scraper, 'requests')
    goinglobal_scraper.requests.status_code.return_value = 999
    goinglobal_scraper.requests.get.return_value = requests.get("https://strayer.wd1.myworkdayjobs.com/en-US/HB_Careers/job/Remote/Python-Software-Engineering-Teaching-Assistant--Part-Time-_R13393")
    final_result = goinglobal_scraper.get_jobs("Software Engineer", "Remote", 5, ['Java', 'Python', 'Coding'])
    assert final_result is not None
