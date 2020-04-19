import json
import os

import requests
import xmltodict
from flask import Flask, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo

from helper.db import create_account

app = Flask(__name__)

BASE_API = 'https://www.boardgamegeek.com/xmlapi2/'
HOT_API = BASE_API + 'hot'
THING_API = BASE_API + 'thing?id='
SEARCH_API = BASE_API + 'search?type=boardgame&query='
root_password = os.environ.get('ROOT_PASSWORD')

app.config["MONGO_URI"] = f'mongodb+srv://root:{root_password}@piercluster-zyykg.mongodb.net/BoardGame?retryWrites=true&w=majority'
mongo = PyMongo(app)
DB=mongo.db

loggedIn = False

@app.route('/')
@app.route('/index')
def index():
    r = requests.get(HOT_API)
    doc = xmltodict.parse(r.content)
    docs=doc["items"]["item"]
    return render_template("pages/index.html", 
                            docs=docs, 
                            loggedIn=loggedIn,
                            title="Home")

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    loggedIn = True if 'user' in session else False

    if loggedIn == True:
        user_in_db = mongo.db.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', username=user_in_db['username']))

    if request.method == 'POST':
        post_request = request.get_json()
        # response = login_req(db, post_request)
        # return json.dumps(response)

    return render_template(
        "pages/login.html",
        loggedIn=loggedIn,
    )

# new account page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    loggedIn = True if 'user' in session else False

    if loggedIn:
        user_in_db = DB.users.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('my_account_page', username=user_in_db['username']))

    if request.method == 'POST':
        post_form = request.form
        response = create_account(DB, post_form)
        return json.dumps(response)

    return render_template(
        'pages/registration.html', 
        loggedIn=loggedIn
    )

@app.route('/search/<query>', methods=['GET'])
def search(query):
    r = requests.get(SEARCH_API+query)
    search_results = xmltodict.parse(r.content)
    search_results=search_results["items"]["item"]
    return render_template("pages/search-results.html",  
                            search_results=search_results, 
                            loggedIn=loggedIn)

@app.route('/game/<id>', methods=['GET'])
def game(id):
    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    detail=detail["items"]["item"]
    return render_template("pages/detail.html", 
                           detail=detail, 
                           loggedIn=loggedIn)

@app.route('/test', methods=['GET'])
def access_db():
    return render_template("pages/sto-gatto.html", 
                            gattos=mongo.db.users.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
