import sqlite3 as sql
from datetime import date

connection = sql.connect('password.db')
cursor = connection.cursor()

createTable = """CREATE TABLE IF NOT EXISTS
passwords(website TEXT PRIMARY KEY, password TEXT, created TEXT, modified TEXT)"""
deleteTable = """DROP TABLE passwords"""
query = """INSERT INTO passwords VALUES('hello', 'underwater', 'today', 'not today')"""

rows = cursor.execute('SELECT * FROM passwords').fetchall()
for row in rows:
    print(row)

def addRecord(domain, password):
    dateCreated = str(date.today())
    dateModified = dateCreated
    hashed = password

    

#addRecord('gmail', 'password')