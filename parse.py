'''
Use this script to print out the id and name of all champions in the game

currently getting data from: http://ddragon.leagueoflegends.com/cdn/13.1.1/data/en_US/champion.json 
change the version number as neccesary
'''

import json

with open('champions.json', encoding="utf8") as file:
    data = json.load(file)

for champ_name in data.get('data'):
    champion = data.get('data').get(champ_name)
    id = champion.get('id')
    key = champion.get('key')
    print(','.join([key, id]))