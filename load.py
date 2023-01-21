import sqlite3
import requests
from dotenv import dotenv_values

API_KEY = dotenv_values(".env").get('API_KEY')

CHAMPIONS = {}
with open('champions.csv') as file:
    for line in file:
        id, name = line.split(',')
        CHAMPIONS[id] = name

def get_player_data(summoner_name) -> list:
    req = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}')
    summoner_id = req.json().get('id')

    print(req.json())

    champions = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={API_KEY}').json()
    champions = [{'championId': champion.get('championId'), 'championPoints': champion.get('championPoints')} for champion in champions]
    return champions

get_player_data('EricTalks')

# qWHmZzjS5fs-5sLuVIE4_SbOocls_FxOI8Z5njtrq_5RWZA
# YaOYiBmx6fNjVdHdsvTS3Z8flqcFiBbY6YKBv9vFZAJlrUKzku_P3z6n7HIDGl9Wp9k580Y-mvyW5A
# https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/YaOYiBmx6fNjVdHdsvTS3Z8flqcFiBbY6YKBv9vFZAJlrUKzku_P3z6n7HIDGl9Wp9k580Y-mvyW5A/ids?start=0&count=20&api_key=RGAPI-3e07a280-10d8-4054-83af-7b687c7759bf