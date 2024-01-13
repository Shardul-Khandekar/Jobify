import pymysql

host = 'srijas.cd1pfgqpboiq.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'adminadmin'
database = 'srijas'

connection = pymysql.connect(host=host, user=user, password=password, database=database)
with connection:
    cur = connection.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print("Database version: {} ".format(version[0]))
