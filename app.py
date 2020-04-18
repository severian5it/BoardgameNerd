import os
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
    return render_template("pages/index.html",  docs=docs, loggedIn=loggedIn)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    loggedIn = True if 'user' in session else False

    if loggedIn == True:
        user_in_db = mongo.db.BoardGame.users.find_one({"username": session['user']})
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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)