import requests
import xmltodict

from flask import url_for
from .. import THING_API

from random import randint




def thumbnail(id):
    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    try:
        thumbnail=detail["items"]["item"].get("thumbnail", url_for('static', filename='img/question-mark.png')) 
    except:
        thumbnail = url_for('static', filename='img/question-mark.png')
    return thumbnail

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
        
