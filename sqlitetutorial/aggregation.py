import sqlite3

class RowSet:
    def __init__(self):
        self.rows = set()

    def step(self, value):
        self.rows.add(value)

    def finalize(self):
        return ';'.join(self.rows)


conn = sqlite3.connect(':memory:')
conn.create_aggregate('row_set', 1, RowSet)

cur = conn.cursor()
cur.execute('CREATE TABLE users (first_name char(20))')
cur.execute(
    """INSERT INTO users(first_name) 
        VALUES ("Ivan"),
                ("Peter"),
                ("Mike"),
                ("Tyson"),
                ("Ivan"),
                ("Jeremy")
    """)
cur.execute('SELECT row_set(first_name) AS result FROM users')
row = cur.fetchall()
print(row)