import requests
import xmltodict

from flask import url_for
from .. import THING_API

from random import randint



def thumbnail(search_ids_to_enrich):
    value = ','.join(search_ids_to_enrich)
    r = requests.get(THING_API+value)
    details = xmltodict.parse(r.content)
    results_list = []
    for d in details['items']['item']:
        result = {}
        result['id'] = d.get('@id')
        result['thumbnail'] = d.get('thumbnail', url_for('static', filename='img/question-mark.png'))
        board_game_name = d.get('name')
        if type(board_game_name) == list:
            result['name'] = board_game_name[0].get('@value')
        else:
            result['name'] = board_game_name.get('@value')
        results_list.append(result)

    print(results_list)
    return results_list

def random_games(nbr=30):
    random_list = []
    for _ in range(nbr):
        value = randint(0, 180000)
        random_list.append(str(value))
    
    random_values = ','.join(random_list)
    filter_type = '&type=boardgame'
    r = requests.get(THING_API+random_values+filter_type)
    details = xmltodict.parse(r.content)
    random_results = []
    for d in details['items']['item']:
        random_results.append(d)

    return random_results
        
