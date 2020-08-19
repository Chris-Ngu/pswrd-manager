# Import hashing function for addRecord

import sqlite3 as sql
from datetime import date

connection = sql.connect('passwordDatabase.db')
cursor = connection.cursor()


def addRecord(domain, password):
    cleanedDomain = domain.upper()
    dateCreated = str(date.today())
    dateModified = dateCreated
    hashed = password

    query = f"INSERT INTO passwords(website, password, created, modified) VALUES ('{cleanedDomain}', '{hashed}', '{dateCreated}', '{dateModified}')"
    try:
        cursor.execute(query)
        connection.commit()
        print('Written to database successfully')
    except Exception as e:
        print('ERROR OCCURED WHILE WRITING TO DATABASE: ' + str(e))


def removeRecord(domain):
    cleanedDomain = domain.upper()

    query = f"DELETE FROM passwords WHERE website = '{cleanedDomain}'"
    try:
        cursor.execute(query)
        connection.commit()
        print('Record has been deleted')
    except Exception as e:
        print('ERROR OCCURED WHILE DELETING TO DATABASE: ' + str(e))


def updateRecord(domain):
    # https://www.mysqltutorial.org/mysql-exists/
    # Check for existing domain, then ask for new password
    cleanedDomain = domain.upper()

    query = f"SELECT website FROM passwords WHERE website = '{cleanedDomain}'"
    if len(cursor.execute(query).fetchall()) == 1:
        print('record found')

    else:
        choice = input('Record not found, please try again...')
        updateRecord(choice)


updateRecord('gmail')
