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
    champions = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={API_KEY}').json()
    champions = [{'championId': champion.get('championId'), 'championPoints': champion.get('championPoints')} for champion in champions]
    return champions
