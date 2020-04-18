from werkzeug.security import generate_password_hash, check_password_hash


def create_account(db, post_request):
    print(db, post_request)
    emailExists = True
    userExists = True

    user_email = db.users.find_one({"email": post_request['email']})
    user_username = db.users.find_one({"username": post_request['username']})

    if not user_email:
        emailExists = False
    elif not user_username:
        userExists = False

    if not user_username and not user_email:
        userExists = False
        emailExists = False
        post_request['password'] = generate_password_hash(post_request['password'])
        db.users.insert_one(post_request)

    response = {
        "emailExists": emailExists,
        "userExists": userExists,
        "username": post_request['username']
    }
    return response