import requests

from importlib.machinery import SourceFileLoader
simplyhired_scraper = SourceFileLoader('simplyhired_scraper', 'code/Scraper/simplyhired_scraper.py').load_module()


def test_simplyhired_scraper_working(mocker):
    ans = simplyhired_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert ans is not None


def test_simplyhired_scraper_notworking(mocker):
    mocker.patch.object(simplyhired_scraper, 'requests')
    simplyhired_scraper.requests.status_code.return_value = 404
    simplyhired_scraper.requests.get.return_value = requests.get("https://www.simplyhired.com/search?q=software+engineer&l=Raleigh")
    ans = simplyhired_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert ans is not None
