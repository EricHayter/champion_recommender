import sqlite3
import requests
from dotenv import dotenv_values

API_KEY = dotenv_values(".env.API_KEY")

summoner_name = 'EricTalks'

def get_player_data(String: summoner_name) -> list:
    req = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}')
    summoner_id = req.json().get('id')
    champions = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={API_KEY}').json()
    return champions

# 

'''
{'id': 'qWHmZzjS5fs-5sLuVIE4_SbOocls_FxOI8Z5njtrq_5RWZA', 'accountId': 'rg-3sBZbshsdTMTC8EuDyotrISKIYdhLI1FSekLbGhHXbA', 'puuid': 'YaOYiBmx6fNjVdHdsvTS3Z8flqcFiBbY6YKBv9vFZAJlrUKzku_P3z6n7HIDGl9Wp9k580Y-mvyW5A', 
'name': 'EricTalks', 'profileIconId': 1455, 'revisionDate': 1673392753000, 'summonerLevel': 194}
'''