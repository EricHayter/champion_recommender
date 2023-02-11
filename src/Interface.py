import requests
from dotenv import dotenv_values

API_KEY = dotenv_values(".env").get('API_KEY')

CHAMPIONS = {}
with open('champions.csv') as file:
    for line in file:
        id, name = line.split(',')
        CHAMPIONS[id] = name

def get_player_puuid(summoner_name) -> str:
    req = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}')
    if req.status_code != 200:
        return None

    return req.json()['puuid']

def get_mastery_data(summoner_id: str) -> dict:
    req = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={API_KEY}')
    if req.status_code == 200:
        return req.json()[:10]

    return None

def get_recent_game(puuid: str) -> str:
    return requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1&api_key={API_KEY}').json()[0]

def get_game_participants(game_id: str) -> tuple:
    req = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{game_id}?api_key={API_KEY}')
    if req.status_code == 200:
        req = req.json()
        participant_puuid = req['metadata']['participants']
        participant_summoner_id = [player['summonerId'] for player in req['info']['participants']]
        return participant_puuid, participant_summoner_id
    else:
        return None

def main():
    print(get_game_participants('NA1_4568390296'))    
    return

if __name__ == "__main__":
    main()