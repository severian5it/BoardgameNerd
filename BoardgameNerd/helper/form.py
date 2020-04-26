from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def check_user_login(db, post_request):
    user = db.users.find_one({'$or': [{ 'username': post_request['username']}, 
                                {'email': post_request['email'] } ]})
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

def change_user_mail(db, post_request):
    wrong_mail = False
    updated = False
    no_user = False

    username = post_request.get('user')
    old_mail= post_request.get('oldemail')
    new_mail = post_request.get('newemail')

    user = db.users.find_one({ 'username': post_request['username']})

    if user:
            db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"mail": post_request["newemail"]}})           
            updated = True
        else:
            wrong_password = True
    else:
       no_user = True             

    response = {
        "wrong_password": wrong_password,
        "updated": updated,
        "no_user": no_user
    }
    return response

def change_user_password(db, post_request):
    wrong_password = False
    updated = False
    no_user = False

    username = post_request.get('user')
    old_password= post_request.get('oldpassword')
    new_password = post_request.get('newpassword')

    user = db.users.find_one({ 'username': post_request['username']})

    if user:
        if check_password_hash(user['password'], post_request['oldpassword']):
            db.users.find_one_and_update({"_id": ObjectId(user["_id"])}, {"$set": {"password": post_request["newpassword"]}})           
            updated = True
        else:
            wrong_password = True
    else:
       no_user = True             

    response = {
        "wrong_password": wrong_password,
        "updated": updated,
        "no_user": no_user
    }
    return response
