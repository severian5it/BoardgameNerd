import requests
import xmltodict

from flask import url_for
from .. import THING_API

from random import randint


def enrich_thumbnail(search_ids_to_enrich):
    """search api doesn't return thumbnail, this procedure will enrich it with more information
    Args:
        search_ids_to_enrich: list of game id to enrich
    Returns:
        list enriched

    """
    value = ','.join(search_ids_to_enrich)
    r = requests.get(THING_API+value)
    details = xmltodict.parse(r.content)
    results_list = []
    for d in details['items']['item']:
        result = {}
        result['id'] = d.get('@id')
        result['image'] = d.get('image', url_for('static', filename='img/question-mark.png'))
        board_game_name = d.get('name')
        if type(board_game_name) == list:
            result['name'] = board_game_name[0].get('@value')
        else:
            result['name'] = board_game_name.get('@value')
        results_list.append(result)

    return results_list

def random_games(nbr=50):
    """creating a list of random games to show on landing page
    Args:
        nbr: number of random games to return
    Returns:
        list of dictionaries containing random games

    """
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
        result = {}
        board_game_name = d.get('name')
        if type(board_game_name) == list:
            result['name'] = board_game_name[0].get('@value')
        else:
            result['name'] = board_game_name.get('@value')
        result['id'] = d.get('@id')
        result['image'] = d.get('image')
        if result['image'] is not None:
            random_results.append(result)
    return random_results[:12]

def wrangle_game(detail):
    """prepare the results of game detail api to be better shown
    Args:
        detail: dictionary returned by API
    Returns:
        list of dictionaries containing random games

    """
    detail=detail["items"]["item"]
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

    return result
        

