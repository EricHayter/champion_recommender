import sqlite3
import time
import Interface

ITERATIONS = 10

with sqlite3.connect('crawl.db') as conn:
    c = conn.cursor()

    for i in range(ITERATIONS):
        print(f'Iteration {i + 1}/{ITERATIONS}')

        c.execute("SELECT * FROM account_queue LIMIT 1")
        summoner_puuid = c.fetchone()[0]

        c.execute("DELETE FROM account_queue WHERE id=?",(summoner_puuid, ))
        c.execute("INSERT INTO visited_accounts (id) VALUES (?)",(summoner_puuid, ))
        c.execute("INSERT INTO players (id,data) VALUES (?,?)",(summoner_puuid, "NA",))
        conn.commit()

        game_id = Interface.get_recent_game(summoner_puuid)
        recent_players = Interface.get_players(game_id)

        for player in recent_players:
            c.execute(""" INSERT INTO account_queue (id)
                SELECT ?
                WHERE NOT EXISTS (SELECT 1 FROM visited_accounts WHERE id=?)
            """, (player, ) * 2)
            c.execute(""" INSERT INTO players (id, data)
                SELECT ?, ?
                WHERE NOT EXISTS (SELECT 1 FROM players WHERE id=?)
            """, (player, "NA", player,))
            conn.commit()

        time.sleep(1)