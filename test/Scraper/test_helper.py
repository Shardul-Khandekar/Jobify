from importlib.machinery import SourceFileLoader
helper = SourceFileLoader('helper', 'code/Scraper/helper.py').load_module()


def test_db_connect(mocker):
    mocker.patch.object(helper, 'open')
    mocker.patch.object(helper.json, 'load')
    helper.json.load.return_value = {
        'server_name': None,
        'user_name': None,
        'password': None,
        'db_name': None
    }

    class mock_connection:
        def __init__(self, host, database, user, password):
            pass

        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return []

    mocker.patch.object(helper.mysql.connector, 'connect', mock_connection)
    connection = helper.db_connect()
    assert type(connection) == mock_connection


def test_get_all_skills(mocker):
    skills = [('Java'), ('Python'), ('C++')]

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return skills

    mocker.patch.object(helper, 'db_connect', mock_connection)

    allskills = helper.get_all_skills()

    for s in skills:
        assert s[0] in allskills


def test_get_all_skills_empty_list(mocker):
    skills = []

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return skills

    mocker.patch.object(helper, 'db_connect', mock_connection)
    allskills = helper.get_all_skills()

    assert allskills == []


def test_extract_skills_empty_description():
    result = helper.extract_skills("", ['Java', 'C++', 'Python'])
    assert result == []


def test_extract_skills_empty_skills():
    result = helper.extract_skills("Java C++ Python", [])
    assert result == []


def test_extract_skills_empty():
    result = helper.extract_skills("", [])
    assert result == []


def test_extract_skills_with_matching():
    result = helper.extract_skills("Java C++", ["Java", "C++", "Python"])
    assert result is not None
    assert result != []
    assert "Java" in result
    assert "C++" in result
    assert "Python" not in result


def test_extract_skills_without_matching():
    result = helper.extract_skills("Windows Soft Skills", ['Java', 'C++', 'Python'])
    assert result == []


def test_matching_skills_both_empty():
    result = helper.matching_skills([], [])
    assert result == []


def test_matching_skills_first_empty():
    result = helper.matching_skills([], ['Java', 'C++', 'Python'])
    assert result == []


def test_matching_skills_second_empty():
    result = helper.matching_skills(['Java', 'C++', 'Python'], [])
    assert result == []


def test_matching_skills_with_matching():
    result = helper.matching_skills(['Java', 'C++', 'Python'], ['Java', 'Python'])
    assert result is not None
    assert result != []
    assert "Java" in result
    assert "C++" not in result
    assert "Python" in result


def test_matching_skills_without_matching():
    result = helper.matching_skills(['C++', 'Spring'], ['Java', 'Python'])
    assert result == []


def test_print_matching_skills_both_empty():
    result = helper.print_matching_skills([], [])
    assert result == ""


def test_print_matching_skills_first_empty():
    result = helper.print_matching_skills([], ['Java', 'C++', 'Python'])
    assert result == ""


def test_print_matching_skills_second_empty():
    result = helper.print_matching_skills(['Java', 'C++', 'Python'], [])
    assert result == ""


def test_print_matching_skills_with_matching():
    result = helper.print_matching_skills(['Java', 'C++', 'Python'], ['Java', 'Python'])
    assert result is not None
    assert result != ""
    assert "Java" in result
    assert "C++" not in result
    assert "Python" in result


def test_print_matching_skills_without_matching():
    result = helper.print_matching_skills(['C++', 'Spring'], ['Java', 'Python'])
    assert result == ""


def test_filter_jobs_matching():
    job = {
        "skills": ['Java', 'C++', 'Python', 'Spring', 'Akka', 'Microservice', 'HTML', 'PHP', 'SQL', 'JQuery']
    }
    user_jobs = {
        "a@a.com": [job]
    }
    user_skills = {
        "a@a.com": ['Java', 'C++', 'Python', 'Spring', 'Akka', 'HTML', 'SQL']
    }
    result = helper.filter_jobs(user_jobs, user_skills)
    assert job in result["a@a.com"]


def test_filter_jobs_not_matching():
    job = {
        "skills": ['Java', 'C++', 'Python', 'Spring', 'Akka', 'Microservice', 'HTML', 'PHP', 'SQL', 'JQuery']
    }
    user_jobs = {
        "a@a.com": [job]
    }
    user_skills = {
        "a@a.com": ['Docker', 'Jenkins', 'Groovy', 'Pipeline', 'CI/CD', 'Kubernetes', 'AWS']
    }
    result = helper.filter_jobs(user_jobs, user_skills)
    assert job not in result["a@a.com"]


def test_filter_jobs_some_matching():
    job1 = {
        "skills": ['Java', 'C++', 'Python', 'Spring', 'Akka', 'Microservice', 'HTML', 'PHP', 'SQL', 'JQuery']
    }
    job2 = {
        "skills": ['Docker', 'CI/CD', 'Jenkins', 'Groovy', 'Microservice', 'HTML', 'PHP', 'SQL', 'JQuery']
    }
    user_jobs = {
        "a@a.com": [job1, job2]
    }
    user_skills = {
        "a@a.com": ['Docker', 'Jenkins', 'Groovy', 'Pipeline', 'CI/CD', 'Kubernetes', 'AWS']
    }
    result = helper.filter_jobs(user_jobs, user_skills)
    assert job1 not in result["a@a.com"]
    assert job2 in result["a@a.com"]


def test_get_user_skills_map_with_common(mocker):
    user_skills_list = [('a@a.com', 'Java'), ('a@a.com', 'Python'), ('a@a.com', 'C++'), ('b@b.com', 'Spring'), ('b@b.com', 'Akka'), ('b@b.com', 'Java')]

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return user_skills_list

    mocker.patch.object(helper, 'db_connect', mock_connection)

    user_skills_map = helper.get_user_skills_map()

    assert 'a@a.com' in user_skills_map.keys()
    assert 'b@b.com' in user_skills_map.keys()
    assert 'Java' in user_skills_map['a@a.com']
    assert 'Python' in user_skills_map['a@a.com']
    assert 'C++' in user_skills_map['a@a.com']
    assert 'Spring' in user_skills_map['b@b.com']
    assert 'Akka' in user_skills_map['b@b.com']
    assert 'Java' in user_skills_map['b@b.com']


def test_get_user_skills_map_without_common(mocker):
    user_skills_list = [('a@a.com', 'Java'), ('a@a.com', 'Python'), ('a@a.com', 'C++'), ('b@b.com', 'Spring'), ('b@b.com', 'Akka')]

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return user_skills_list

    mocker.patch.object(helper, 'db_connect', mock_connection)

    user_skills_map = helper.get_user_skills_map()

    assert 'a@a.com' in user_skills_map.keys()
    assert 'b@b.com' in user_skills_map.keys()
    assert 'Java' in user_skills_map['a@a.com']
    assert 'Python' in user_skills_map['a@a.com']
    assert 'C++' in user_skills_map['a@a.com']
    assert 'Spring' in user_skills_map['b@b.com']
    assert 'Akka' in user_skills_map['b@b.com']


def test_get_user_skills_map_one_user(mocker):
    user_skills_list = [('a@a.com', 'Java'), ('a@a.com', 'Python'), ('a@a.com', 'C++')]

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return user_skills_list

    mocker.patch.object(helper, 'db_connect', mock_connection)

    user_skills_map = helper.get_user_skills_map()

    assert 'a@a.com' in user_skills_map.keys()
    assert 'Java' in user_skills_map['a@a.com']
    assert 'Python' in user_skills_map['a@a.com']
    assert 'C++' in user_skills_map['a@a.com']


def test_get_user_skills_map_empty_list(mocker):
    user_skills_list = []

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return user_skills_list

    mocker.patch.object(helper, 'db_connect', mock_connection)

    user_skills_map = helper.get_user_skills_map()

    assert user_skills_map == {}


def test_match_percentage_both_empty():
    result = helper.match_percentage([], [])
    assert result == "0.0%"


def test_match_percentage_first_empty():
    result = helper.match_percentage([], ['Java', 'C++', 'Python'])
    assert result == "0.0%"


def test_match_percentage_second_empty():
    result = helper.match_percentage(['Java', 'C++', 'Python'], [])
    assert result == "0.0%"


def test_match_percentage_with_matching():
    result = helper.match_percentage(['Java', 'Python'], ['Java', 'C++', 'Python'])
    assert result == "66.67%"


def test_match_percentage_without_matching():
    result = helper.match_percentage(['C++', 'Spring'], ['Java', 'Python'])
    assert result == "0.0%"
