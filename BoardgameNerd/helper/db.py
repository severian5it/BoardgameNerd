from werkzeug.security import generate_password_hash, check_password_hash

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