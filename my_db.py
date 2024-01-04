import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12Mostwanted20'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute('CREATE DATABASE my_database')

print('All done')
