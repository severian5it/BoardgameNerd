import requests
import xmltodict

from flask import url_for
from .. import THING_API


def thumbnail(id):
    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    try:
        thumbnail=detail["items"]["item"].get("thumbnail", url_for('static', filename='img/question-mark.png')) 
    except:
        thumbnail = url_for('static', filename='img/question-mark.png')
    return thumbnail