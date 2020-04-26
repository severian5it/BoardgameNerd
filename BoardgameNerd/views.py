import json
import requests
import xmltodict

from .helper.db import create_account, insert_in_collection, delete_from_collection
from .helper.form import check_user_login, change_user_password, change_user_mail
from . import app, HOT_API, SEARCH_API, THING_API, DB
from flask import redirect, render_template, request, session, url_for


@app.route('/')
@app.route('/index')
def index():
    loggedIn = True if 'user' in session else False
    user = session.get('user')
    r = requests.get(HOT_API)
    doc = xmltodict.parse(r.content)
    docs=doc["items"]["item"]
    return render_template("pages/index.html", 
                            docs=docs, 
                            loggedIn=loggedIn,
                            title="Home",
                            user=user)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    loggedIn = True if 'user' in session else False
    user = session.get('user')

    if loggedIn == True:
        user_in_db = DB.users.find_one({"username": session["user"]})
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
        user=user
    )

# new account page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    loggedIn = True if 'user' in session else False
    user = session.get('user')

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
        loggedIn=loggedIn,
         user=user
    )

# search page
@app.route('/search/<query>', methods=['GET'])
def search(query):
    loggedIn = True if 'user' in session else False
    user = session.get('user')

    r = requests.get(SEARCH_API+query)
    search_results = xmltodict.parse(r.content)
    search_results=search_results["items"]["item"]
    return render_template("pages/search-results.html",  
                            search_results=search_results, 
                            loggedIn=loggedIn,
                            user=user)

# login page
@app.route('/game/<id>', methods=['GET', 'POST'])
def game(id):
    loggedIn = True if 'user' in session else False
    user = session.get('user')

    if request.method == 'POST':
        post_form = request.form
        response = insert_in_collection(DB, post_form)
        return json.dumps(response)
    else:    
        r = requests.get(THING_API+str(id))
        detail = xmltodict.parse(r.content)
        detail=detail["items"]["item"]
        return render_template("pages/detail.html", 
                            detail=detail, 
                            loggedIn=loggedIn,
                            user=user,
                            id=id)

@app.route('/collection', methods=['GET', 'POST'])
def collection():
    loggedIn = True if 'user' in session else False
    user = session.get('user')

    if request.method == 'POST':
        post_form = request.form
        response = delete_from_collection(DB, post_form)
        return json.dumps(response)
    else:
        return render_template("pages/collection.html", 
                            loggedIn=loggedIn,
                                user=user,
                                collections=DB.collection.find({"username":user}))


# log out page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# change password and mail
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    loggedIn = True if 'user' in session else False
    user = session.get('user')

    if request.method == 'POST':
        post_request = request.form
        print(post_request)
        if post_request.get('oldemail') != post_request.get('newemail'):
                response = change_user_mail(DB, post_request)
                return json.dumps(response)
        
        if post_request.get('oldpassword') != post_request.get('newpassword'):
                response = change_user_password(DB, post_request)
                return json.dumps(response)
    else:
        return render_template(
            "pages/settings.html", 
            loggedIn=loggedIn,
            user=user
        )

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_erro(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


