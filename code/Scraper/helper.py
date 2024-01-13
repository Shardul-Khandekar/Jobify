import mysql.connector
import json


MATCH_THRESHOLD = 1


def db_connect():
    properties = open('parameters.json')
    data = json.load(properties)
    server_name = data['server_name']
    user_name = data['user_name']
    password = data['password']
    db_name = data['db_name']
    connection = mysql.connector.connect(host=server_name, database=db_name, user=user_name, password=password)
    return connection


def get_all_skills():
    connection = db_connect()
    sql_select_Query = "select DISTINCT skill_title from skill_master"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    all_skills = []
    for row in records:
        all_skills.append(row[0])
    return all_skills


def extract_skills(desc, skills):
    res = []
    desc = desc.upper()
    for s in skills:
        if s.upper() in desc:
            res.append(s)
    return res


def matching_skills(skills1, skills2):
    return list(set(skills1) & set(skills2))


def match_percentage(user_skills, job_skills):
    if len(job_skills) == 0:
        return "0.0%"
    return str(round((len(matching_skills(user_skills, job_skills)) / len(job_skills)) * 100, 2)) + "%"


def print_matching_skills(skills1, skills2):
    return ', '.join(matching_skills(skills1, skills2))


def get_user_skills_map():
    connection = db_connect()
    query = "select um.user_email, sm.skill_title from user_master um, user_resume ur, resume_skills rs, skill_master sm where um.user_id = ur.user_id and ur.resume_id = rs.resume_id and rs.skill_id = sm.skill_id"
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    res = {}
    for r in records:
        if r[0] not in res.keys():
            res[r[0]] = []
        res[r[0]].append(r[1])
    return res


def filter_jobs(user_jobs, user_skills):
    filtered_user_jobs = {}
    for user in user_jobs.keys():
        skills = user_skills[user]
        filtered_jobs = []
        for job in user_jobs[user]:
            job_skills = job['skills']
            if (len(matching_skills(job_skills, skills))) >= MATCH_THRESHOLD:
                filtered_jobs.append(job)
        filtered_user_jobs[user] = filtered_jobs
    return filtered_user_jobs
