import requests

from importlib.machinery import SourceFileLoader
indeed_scraper = SourceFileLoader('indeed_scraper', 'code/Scraper/indeed_scraper.py').load_module()


def test_indeed_scraper_working(mocker):
    ans = indeed_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    print(ans)
    assert ans is not None


def test_indeed_scraper_nonworking(mocker):
    mocker.patch.object(indeed_scraper, 'requests')
    indeed_scraper.requests.status_code.return_value = 999
    indeed_scraper.requests.get.return_value = requests.get("https://www.indeed.com/jobs?q=software%20engineer&l=Raleigh&vjk=2c673ec214d1c981")
    ans = indeed_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert ans is not None
