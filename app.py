import requests
import xmltodict
from flask import Flask, redirect, render_template, request, url_for, session
app = Flask(__name__)

HOT_API = 'https://www.boardgamegeek.com/xmlapi2/hot'

loggedIn = False

@app.route('/')
@app.route('/index')
def index():
    r = requests.get(HOT_API)
    doc = xmltodict.parse(r.content)
    docs=doc["items"]["item"]
    return render_template("index.html",  docs=docs, loggedIn=loggedIn)