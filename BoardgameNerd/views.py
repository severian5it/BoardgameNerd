import json
import requests
import xmltodict
import time

from .helper.db import create_account, insert_in_collection, delete_from_collection, update_collection
from .helper.form import check_user_login, change_user_password, change_user_mail
from .helper.api import enrich_thumbnail, random_games, wrangle_game
from . import app, HOT_API, SEARCH_API, THING_API, DB
from flask import flash, redirect, render_template, request, session, url_for


@app.route('/')
@app.route('/index')
def index():
    """Main access to the application
    Returns:
        rendering landing page

    """
    user = session.get('user')
    r = requests.get(HOT_API)
    doc = xmltodict.parse(r.content)
    docs=doc["items"]["item"]

    r = requests.get(HOT_API)
    doc = xmltodict.parse(r.content)
    docs=doc["items"]["item"]

    random_games_list = random_games()

    return render_template("pages/index.html", 
                            docs=docs,
                            random_games=random_games_list,
                            title="Home",
                            user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Page
    Returns:
        rendering login page

    """
    user = session.get('user')

    if user is not None:
        flash("you are already logged on!")
        return redirect(url_for('collection'))

    if request.method == 'POST':
        post_form = request.form
        response = check_user_login(DB, post_form)
        if response['passwordCorrect']:
            flash("succesful logon!")
            return redirect(url_for('collection'))
        else:
            flash("wrong user or password!")

    return render_template(
        "pages/login.html",
        user=user
    )

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """Registration Page
    Returns:
        rendering registration page

    """
    user = session.get('user')

    if user is not None:
        flash("you are already logged on!")
        return redirect(url_for('collection'))

    if request.method == 'POST':
        post_form = request.form
        response = create_account(DB, post_form)
        if response['user_created']:
            flash('You were successfully signed up')
            return redirect(url_for('login'))
        else:
            flash('user or mail already exists!')

    return render_template(
        'pages/registration.html', 
         user=user
    )

@app.route('/search/<query>', methods=['GET'])
def search(query):
    """Search page
    Args:
        query: word to search for, accept multiple words joined with '+'
    Returns:
        rendering search page results

    """
    user = session.get('user')

    r = requests.get(SEARCH_API+query)
    search_results = xmltodict.parse(r.content)
    if search_results["items"].get("item") is None:
        flash("search returned no result")
    else:    
        search_results=search_results["items"]["item"]

        search_ids_to_enrich = [search['@id'] for search in search_results]
        search_results = enrich_thumbnail(search_ids_to_enrich)

    return render_template("pages/search-results.html",  
                            search_results=search_results, 
                            user=user)

@app.route('/game/<id>', methods=['GET', 'POST'])
def game(id):
    """game detail page
    Args:
        id: id of the game
    Returns:
        rendering detail page

    """
    user = session.get('user')

    if request.method == 'POST':
        if user is None:            
            flash("please login first to add to you collection!")
            return redirect(url_for('login'))

        post_form = request.form
        response = insert_in_collection(DB, post_form)
        if response["inserted"]:
            flash("game added to the collection!")
            return redirect(url_for('index'))
        else:
            flash("this game is already part of your collection!")

    r = requests.get(THING_API+str(id))
    detail = xmltodict.parse(r.content)
    detail = wrangle_game(detail)
    return render_template("pages/detail.html", 
                            detail=detail, 
                            user=user,
                            id=id)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    """game in collection id page
    Args:
        id: id of the game
    Returns:
        rendering game in collection page

    """
    user = session.get('user')

    if user is None:            
        flash("please login first to edit your collection!")
        return redirect(url_for('login'))

    if request.method == 'POST':
        post_form = request.form
        if post_form['type'] == 'delete':
            response = delete_from_collection(DB, post_form)
            if response['deleted']:
                flash("game successfully removed from the collection")
                return redirect(url_for('collection'))
        elif post_form['type'] == 'update':
            response = update_collection(DB, post_form)
            if response['updated']:
                flash("game successfully updated")
                return redirect(url_for('collection'))
  
    detail  = DB.collection.find_one({"username": user, "id":id}) 
    return render_template("pages/edit.html", 
                            detail=detail , 
                            user=user,
                            id=id)

@app.route('/collection', methods=['GET', 'POST'])
def collection():
    """user collection page
    Returns:
        collection for logged user

    """
    user = session.get('user')

    if user is None:            
        flash("please login first to see your collection!")
        return redirect(url_for('login'))

    if request.method == 'POST':
        post_form = request.form
        response = delete_from_collection(DB, post_form)
        if response['deleted']:
            flash("game successfully removed from the collection")
            return redirect(url_for('collection'))
    else:
        return render_template("pages/collection.html", 
                                user=user,
                                collections=DB.collection.find({"username":user}))


@app.route('/logout')
def logout():
    """logout function
    Returns:
        redirect to index cleaning the session.

    """
    session.clear()
    return redirect(url_for('index'))



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    """setting pages
    Returns:
        render setting page for logged user

    """
    user = session.get('user')

    if request.method == 'POST':
        post_request = request.form
        if post_request.get('oldemail') != post_request.get('newemail'):
                response = change_user_mail(DB, post_request)
                if response['updated']:
                    flash("mail successfully updated")
        
        if post_request.get('oldpassword') != post_request.get('newpassword'):
                response = change_user_password(DB, post_request)
                if response['updated']:
                    flash("password successfully updated")

    return render_template(
        "pages/settings.html", 
        user=user
    )

@app.errorhandler(404)
def page_not_found(e):
    """not found page
    Args:
        e: exception causing the page to be shown
    Returns:
        render not found page

    """
    return render_template('pages/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """error pages
    Args:
        e: exception causing the page to be shown
    Returns:
        render error page

    """
    return render_template('pages/500.html'), 500


