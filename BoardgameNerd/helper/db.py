from werkzeug.security import generate_password_hash

def create_account(db, post_form):
    emailExists = True
    userExists = True
    email = post_form['email']
    user = post_form['username']
    password = post_form['password']

    user_email = db.users.find_one({"email": email})
    user_username = db.users.find_one({"username": user})

    if not user_email:
        emailExists = False
    elif not user_username:
        userExists = False

    if not user_username and not user_email:
        userExists = False
        emailExists = False
        password = generate_password_hash(password)
        db.users.insert_one({'username': user,
                            'email': email,
                            'password': password})

    response = {
        "emailExists": emailExists,
        "userExists": userExists,
        "username": user
    }
    return response

def insert_in_collection(db, post_request):
    is_there_already = False
    inserted = False
    user = post_request['user']
    id = post_request['id']
    boardgame_name = post_request['boardgameName']
    boardgame_description = post_request['boardgameDescription']
    boardgame_image = post_request['boardgameImage']
    boardgame_thumbnail = post_request['boardgameThumbnail']
    boardgame_minplay = post_request['boardgameMinPlayer']
    boardgame_maxplay = post_request['boardgameMaxPlayer']
    boardgame_minage = post_request['boardgameMinAge']
    boardgame_playtime = post_request['boardgameplayingTime']


    boardgame = db.collection.find_one({"username": user, 'id': id})

    if boardgame:
        is_there_already = True
    else:
        db.collection.insert_one({'username': user,
        'id': id,
        'boardgame_name': boardgame_name,
        'boardgame_description': boardgame_description,
        'boardgame_image': boardgame_image,
        'boardgame_thumbnail': boardgame_thumbnail,
        'boardgame_minplay': boardgame_minplay,   
        'boardgame_maxplay': boardgame_maxplay,
        'boardgame_minage': boardgame_minage,          
        'boardgame_playtime': boardgame_playtime })

        inserted =True

    response = {
        "isThereAlready": is_there_already,
        "inserted": inserted
    }
    return response

def delete_from_collection(db, post_request):
    deleted = False
    user = post_request['user']
    id = post_request['id']

    test = db.collection.delete_one({'username': user,
    'id': id})
    deleted = True

    response = {
        "deleted": deleted
            }
    return response