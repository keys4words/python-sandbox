import sqlite3

conn = sqlite3.connect('db.sqlite3')

# conn.execute('CREATE TABLE "users" (id, first_name, last_name, birthday)')
# conn.execute('SELECT * FROM "users"')
conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday)
    VALUES (1, "Ivan", "Ivanov", "09-11-1984")
    """
)
conn.execute(
    """INSERT INTO users(id, first_name, last_name, birthday)
    VALUES (2, "Peter", "Petrov", "10-01-1989"),
            (3, "Mike", "Tyson", "25-05-1974")
    """
)

# users = conn.execute('SELECT * FROM "users"').fetchall()
# print(users)
# cursor = conn.execute('SELECT * FROM "users";')
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# cursor.close()

# try:
#     cursor = conn.execute('SELECT * FROM "something";')
# except sqlite3.OperationalError as e:
#     print(e)

# first_name = 'Peter'
# sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name,)
# print(sql_text)
# first_name = '"Peter"'
# sql_text = 'SELECT * FROM users WHERE first_name = "%s"' % (first_name,)
# print(sql_text)
sql_text = 'SELECT * FROM "users" WHERE id = %s' % (1,)
print(sql_text)
sql_text2 = 'SELECT * FROM "users" WHERE id = %s' % ('0 or id like "%"',)
print(sql_text2)

# res = conn.execute(sql_text2).fetchall()
# res = conn.execute('SELECT * FROM "users" WHERE id = ?', (2, )).fetchall()
res = conn.execute('SELECT * FROM "users" WHERE id = :id', {'id': 3}).fetchall()
print(res)
conn.close()