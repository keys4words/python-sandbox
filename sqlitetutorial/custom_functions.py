import sqlite3

def upper_word(raw):
    return raw.upper()


conn = sqlite3.connect(':memory:')
conn.create_function('upper', 1, upper_word)
cur = conn.cursor()

cur.execute('CREATE TABLE users (first_name char(20))')
cur.execute('INSERT INTO users(first_name) VALUES ("Ivan"), ("Peter"), ("Mike")')
cur.execute('SELECT upper(first_name) FROM users')
row = cur.fetchall()
print(row)