from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def check_user_login(db, post_request):
    """check if a user is inserting correct login
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    username = post_request.get('username')
    password = post_request.get('password')
    user = db.users.find_one({'$or': [{ 'username': username}, 
                                {'email': username} ]})
    passwordCorrect = False

    if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            passwordCorrect = True    

    response = {
        "passwordCorrect": passwordCorrect,
        "username": username
    }

    return response

def change_user_mail(db, post_request):
    """change user mail
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    wrong_email = False
    updated = False

    username = post_request.get('user')
    old_mail= post_request.get('oldemail')
    new_mail = post_request.get('newemail')
    mail = db.users.find_one({ 'username': username, 'email': old_mail})
    if mail:
            db.users.find_one_and_update({"username": username}, {"$set": {"email": new_mail}})           
            updated = True
    else:
        wrong_email= True           

    response = {
        "wrong_password": wrong_email,
        "updated": updated
    }
    return response

def change_user_password(db, post_request):
    """change user passworc
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    wrong_password = False
    updated = False
    no_user = False

    username = post_request.get('user')
    old_password= post_request.get('oldpassword')
    new_password = generate_password_hash(post_request.get('newpassword'))

    user = db.users.find_one({ 'username': username})
    if user:
        if check_password_hash(user['password'], old_password):
            db.users.find_one_and_update({"username": username}, {"$set": {"password": new_password}})           
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
