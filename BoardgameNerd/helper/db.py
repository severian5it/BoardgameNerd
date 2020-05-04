from werkzeug.security import generate_password_hash

def create_account(db, post_form):
    """register new user
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    user_created = False
    email = post_form['email']
    user = post_form['username']
    password = post_form['password']

    user_email = db.users.find_one({"email": email})
    user_username = db.users.find_one({"username": user})

    print(user_email, user_username)
    if not user_email and not user_username:
        print('here')
        password = generate_password_hash(password)
        db.users.insert_one({'username': user,
                            'email': email,
                            'password': password})
        user_created = True

    response = {
        "user_created": user_created
    }
    return response

def insert_in_collection(db, post_request):
    """insert a game in a user's collection
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
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
    boardgame_yearpublished = post_request['boardgameYearPublished']
    boardgame_playtime = post_request['boardgameplayingTime']
    boardgame_family = post_request['boardgamefamily'].split(',')
    boardgame_category = post_request['boardgamecategory'].split(',')
    boardgame_mechanic = post_request['boardgamemechanic'].split(',')
    boardgame_designer = post_request['boardgamedesigner'].split(',')

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
        'boardgame_playtime': boardgame_playtime,
        'year_published': boardgame_yearpublished,
        'boardgame_family': boardgame_family,   
        'boardgame_category': boardgame_category,
        'boardgame_mechanic': boardgame_mechanic,          
        'boardgame_designer': boardgame_designer})

        inserted =True

    response = {
        "is_there_already": is_there_already,
        "inserted": inserted
    }
    return response

def delete_from_collection(db, post_request):
    """remove a game in a user's collection
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    deleted = False
    user = post_request['user']
    id = post_request['id']

    db.collection.delete_one({'username': user,
    'id': id})
    deleted = True

    response = {
        "deleted": deleted
            }
    return response

def update_collection(db, post_request):
    """update a game in user's collection
    Args:
        db: database to check for account 
        post_form: form from which extract detail
    Returns:
        response dictionary containing the result of operations

    """
    updated = False
    user = post_request['user']
    id = post_request['id']
    note = post_request['note']
    date_buy = post_request['dateBuy']
    rating = post_request['rating']
    db.collection.find_one_and_update(
        {'username': user,
        'id': id},
    { "$set": {"note": note, 'dateBuy': date_buy, 'rating': rating}}
    )
    updated = True

    response = {
        "updated": updated
            }

    return response