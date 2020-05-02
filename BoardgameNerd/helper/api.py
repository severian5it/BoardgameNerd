import requests
import xmltodict

from flask import url_for
from .. import THING_API

from random import randint



def enrich_thumbnail(search_ids_to_enrich):
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

def wrangle_game(detail):
    detail=detail["items"]["item"]
    print(detail)
    result = {}
    result['id'] = detail.get('@id')
    result['thumbnail'] = detail.get('thumbnail', url_for('static', filename='img/question-mark.png'))
    board_game_name = detail.get('name')
    if type(board_game_name) == list:
        result['name'] = board_game_name[0].get('@value')
    else:
        result['name'] = board_game_name.get('@value')
    result['description'] = detail.get('description')
    result['thumbnail'] = detail.get('thumbnail')
    result['image'] = detail.get('image')
    result['yearpublished'] = detail.get('yearpublished').get('@value')
    result['minplayers'] = detail.get('minplayers').get('@value')
    result['maxplayers'] = detail.get('maxplayers').get('@value')
    result['minage'] = detail.get('minplayers').get('@value')
    result['playingtime'] = detail.get('playingtime').get('@value')

    characteristict = [(l.get('@type'), l.get('@value'))  for l in detail.get('link')]
    result['boardgamefamily'] = [c[1] for c in characteristict if c[0] == 'boardgamefamily']
    result['boardgamecategory'] = [c[1] for c in characteristict if c[0] == 'boardgamecategory']
    result['boardgamemechanic'] = [c[1] for c in characteristict if c[0] == 'boardgamemechanic']
    result['boardgamedesigner'] = [c[1] for c in characteristict if c[0] == 'boardgamedesigner']



    print(result)
    return result
        

