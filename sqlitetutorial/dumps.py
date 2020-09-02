import os, sqlite3

conn = sqlite3.connect('db3.sqlite3')
conn.execute(
    """CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name,
        last_name,
        birthday
    )"""
)
conn.execute(
    """
    INSERT INTO users(id, first_name, last_name, birthday)
    VALUES (1, "Ivan", "Ivanov", "09-11-1985"),
            (2, "Peter", "Petrov", "01-02-1985"),
            (3, "Myke", "Tyson", "01-02-1985"),
            (4, "John", "Rollings", "01-02-1985"),
            (5, "Harry", "Potter", "01-02-1985")
    """)

with open('db3-dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")