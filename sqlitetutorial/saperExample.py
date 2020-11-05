import sqlite3

# with sqlite3.connect('saper.db') as con:
    # cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    #     /*user_id INTEGER PRIMARY KEY AUTOINCREMENT,*/
    #     name TEXT NOT NULL,
    #     sex INTEGER NOT NULL DEFAULT 1,
    #     old INTEGER,
    #     score INTEGER
    # )""")
    # cur.execute("SELECT * FROM users WHERE score > 900 ORDER BY score DESC")
    # fetchall - list
    # res = cur.fetchall()
    # res = cur.fetchone()
    # print(res)

    # print('='*35)
    # iteration throug list
    # for el in cur:
        # print(el)

    # print('='*35)
    # cur.execute("SELECT * FROM users WHERE score == ORDER BY score DESC")
    # fetchmany(size)

def getUser(score):
    with sqlite3.connect('saper.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE score == {score}")
        return cur.fetchone()


print(getUser(2500))
    