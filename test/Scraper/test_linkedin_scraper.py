from importlib.machinery import SourceFileLoader
linkedin_scraper = SourceFileLoader('linkedin_scraper', 'code/Scraper/linkedin_scraper.py').load_module()


class temp_request:
    def __init__(self, status_code, content, text):
        self.status_code = status_code
        self.content = content
        self.text = "test text for description"


def test_get_jobs(mocker):
    # time.sleep(20)
    text = ""
    with open("test/Scraper/linkedin_test_page.html", "r", encoding='utf-8') as f:
        text = f.read()
    x = temp_request(200, text, "")
    mocker.patch.object(linkedin_scraper, 'requests')
    linkedin_scraper.requests.get.return_value = x

    jobs = linkedin_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert jobs is not None


def test_get_jobs_nonworking(mocker):
    text = ""
    with open("test/Scraper/linkedin_test_page.html", "r", encoding='utf-8') as f:
        text = f.read()
    x = temp_request(900, text, "")

    mocker.patch.object(linkedin_scraper, 'requests')
    linkedin_scraper.requests.get.return_value = x

    jobs = linkedin_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert jobs is not None
