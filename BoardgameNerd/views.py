import json
import requests
import xmltodict

from .helper.db import create_account
from .helper.form import check_user_login
from . import app, HOT_API, SEARCH_API, THING_API, DB
from flask import redirect, render_template, request, session, url_for


@app.route('/')
@app.route('/index')
def index():
    loggedIn = True if 'user' in session else False
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
    print(session, loggedIn)

    if loggedIn == True:
        user_in_db = DB.users.find_one({"username": session["user"]})
        print(user_in_db)
        if user_in_db:
            return render_template("pages/account-page.html", 
                            username=user_in_db.get('username'))

    if request.method == 'POST':
        post_form = request.form
        response = check_user_login(DB, post_form)
        return json.dumps(response)

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
    loggedIn = True if 'user' in session else False

    r = requests.get(SEARCH_API+query)
    search_results = xmltodict.parse(r.content)
    search_results=search_results["items"]["item"]
    return render_template("pages/search-results.html",  
                            search_results=search_results, 
                            loggedIn=loggedIn)

@app.route('/game/<id>', methods=['GET'])
def game(id):
    loggedIn = True if 'user' in session else False

    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    detail=detail["items"]["item"]
    return render_template("pages/detail.html", 
                           detail=detail, 
                           loggedIn=loggedIn)

@app.route('/test', methods=['GET'])
def access_db():
    return render_template("pages/sto-gatto.html", 
                            gattos=DB.users.find())

# log out page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


