import sqlite3

conn = sqlite3.connect('db2.sqlite3')
# conn.execute(
#     """CREATE TABLE users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name,
#         last_name,
#         birthday
#     )
#     """
# )
conn.execute("""
    INSERT INTO users(id, first_name, last_name, birthday)
    VALUES (1, "Ivan", "Ivanov", "09-11-1985"),
            (2, "Peter", "Petrov", "01-02-1985")
""")

conn.row_factory = sqlite3.Row
users = conn.execute('SELECT * FROM users').fetchall()
print(users[0]['BIRthday'])