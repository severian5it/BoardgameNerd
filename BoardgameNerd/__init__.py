import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
BASE_API = 'https://www.boardgamegeek.com/xmlapi2/'
HOT_API = BASE_API + 'hot'
THING_API = BASE_API + 'thing?id='
SEARCH_API = BASE_API + 'search?type=boardgame&query='
ROOT_PASSWORD = os.environ.get('ROOT_PASSWORD')

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
DB=mongo.db
