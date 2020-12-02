from flask import request
from dream_api.rest import bp
from dream_api.user_case.login import Login
# from dream_api.object.req_object import req

@bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json('user_email')
        password = request.json('password')

    except IndexError:
        return 'Method not allowd', 405

    try:
        login=Login(email)
        login_password=login.user_login_info()
        if login_password == password:
            return 'True', 200

        else:
            return 'Password not incorect!', 404

    
    except Exception:
        return 'User not found', 404