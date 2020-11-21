import mysql.connector

db = mysql.connector.connect(
    host='localhost'
    ,user='root'
    ,password='12345'
    ,database='python'
)

# print(db)
cursor = db.cursor()

# cursor.execute("CREATE DATABASE python;")
# cursor.execute("SHOW DATABASES")
# for el in cursor:
#     print(el)

cursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(10));')
cursor.execute('SHOW TABLES;')
for el in cursor:
    print(el)