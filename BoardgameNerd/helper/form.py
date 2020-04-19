from werkzeug.security import check_password_hash
from flask import session

def check_user_login(db, post_request):
    user = db.users.find_one({'$or': [{ 'username': post_request['username']}, 
                                {'email': post_request['username'] } ]})
    passwordCorrect = False
    username = ''

    if user: 
        if check_password_hash(user['password'], post_request['password']):
            session['user'] = user['username']
            passwordCorrect = True    
            username = user['username']    

    response = {
        "userMatch": True if user else False,
        "passwordCorrect": passwordCorrect,
        "username": username
    }

    return response