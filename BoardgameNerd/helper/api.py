import requests
import xmltodict

from flask import url_for
from .. import THING_API

from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers



def thumbnail(id):
    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    try:
        thumbnail=detail["items"]["item"].get("thumbnail", url_for('static', filename='img/question-mark.png')) 
    except:
        thumbnail = url_for('static', filename='img/question-mark.png')
    return thumbnail

def random_games(nbr=15):
    random_list = []
    for _ in range(nbr):
        value = randint(0, 180000)
        r = requests.get(THING_API+str(value))
        detail = xmltodict.parse(r.content)
        if detail.get("items").get('item') is not None:
            detail=detail["items"]["item"]
            random_list.append(detail)

    return random_list
        
