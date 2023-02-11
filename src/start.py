import sqlite3

with sqlite3.connect('crawl.db') as conn:
    c = conn.cursor()

    c.execute("""CREATE TABLE account_queue (
        id text
    )""")

    c.execute("""CREATE TABLE visited_accounts (
        id text
    )""")

    c.execute("""CREATE TABLE players (
        id text,
        data text
    )""")