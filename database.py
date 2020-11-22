import sqlite3 as sql
import bcrypt
import time
from datetime import date


connection = sql.connect('passwordDatabase.db')
cursor = connection.cursor()


def addRecord(domain, password):
    '''
    @args       [domain] : string \n
    @args       [password] : string \n
    @desc       Takes a domain name and password combination to create a new record \n
    @returns    None \n
    '''

    cleanedDomain = domain.upper()
    dateCreated = str(date.today())
    dateModified = dateCreated
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    query = f"""
                INSERT INTO passwords(website, password, created, modified)
                VALUES ('{cleanedDomain}', '{hashed}',
                        '{dateCreated}', '{dateModified}')
            """
    try:
        cursor.execute(query)
        connection.commit()
        print('Written to database successfully')
    except Exception as e:
        print('ERROR OCCURED WHILE WRITING TO DATABASE: ' + str(e))


def removeRecord(domain):
    '''
    @args       [domain] : string \n
    @desc       Takes a string and checks db file to delete record \n
    @returns    None \n
    '''

    cleanedDomain = domain.upper()
    if(checkIfRecordExists(cleanedDomain)):
        query = f"""
                    DELETE FROM passwords
                    WHERE website = '{cleanedDomain}'
                """

        try:
            cursor.execute(query)
            connection.commit()
            print('Record has been deleted sucessfully')
            print('Showing updated records...')
            time.sleep(2)
            showRecords()
            
        except Exception as e:
            print('ERROR OCCURED WHILE DELETING TO DATABASE: ' + str(e))
    else:
        print("Record does not exist")

def updateRecord(domain):
    '''
    @args       [domain] : string \n
    @desc       Takes a string and checks db file to see if a record exists \n
    @returns    None \n
    @refs       https://www.mysqltutorial.org/mysql-exists/
    '''

    cleanedDomain = domain.upper()
    if (checkIfRecordExists(cleanedDomain)):
        print('record found')

        newPassword = input('Enter a new password combination for this record')
        hashed = bcrypt.hashpw(newPassword.encode(), bcrypt.gensalt()).decode()
        today = str(date.today())

        try:
            query = f"""
                        UPDATE passwords
                        SET password = '{hashed}', modified = '{today}'
                        WHERE website = '{cleanedDomain}'
                    """
            cursor.execute(query)
            connection.commit()
            print('Updated existing record successfully')
        except Exception as e:
            print('ERROR OCCURED WHILE WRITTING TO DATABASE: ' + str(e))

    else:
        choice = input('Record not found, please try again...')
        updateRecord(choice)

def showRecords():
    '''
    @desc       Display all records in passwords Table of database \n
    @returns    None \n
    '''
    print("Loading...")
    time.sleep(3)
    print("DOMAIN\tHashed\tCreatedOn\tModifiedOn");
    
    query = f"""
                SELECT *
                FROM passwords
            """

    rows = cursor.execute(query).fetchall()
    for row in rows:
        print(row)

def checkIfRecordExists(domainName):
    '''
    @desc       Checks if a record exists in the PASWORDS table
    @params     String: Domain name
    @returns    Boolean if anything has been found
    '''
    domainName = domainName.upper()

    try:
        query = f"""
                    SELECT COUNT(*)
                    FROM passwords
                    WHERE website = '{domainName}'
                """
        if (cursor.execute(query).fetchall()[0][0] == 1):
            return True
        else:
            return False

    except Exception as e:
        print('ERROR OCCURED WHILE TRYING TO CHECK DOCUMENT EXISTANCE: ' + str(e))

