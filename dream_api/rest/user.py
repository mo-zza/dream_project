from flask import request
from dream_api.rest import bp
from dream_api.user_case.user import Users
# from dream_api.object.req_object import req


@bp.route('/user', methods=['POST'])
def create_user():
    try:
        req_data = request.get_json()

        name=req_data['name']
        email=req_data['email']
        password=req_data['password']
        birth=req_data['birth']
        phone=req_data['phone']
        school=req_data['school']
        address=req_data['address']

    
    except IndexError:

        return 'Method not allowed', 405

    users=Users(email)

    try:
        users.create_user(name, password, birth, phone, school, address)
        return 'True', 200
    except Exception:
        return 'User already exist', 400

        

@bp.route('/user', methods=['GET'])
def search_user():
    try:
        data = request.get_json()
        email = data['email']

    except IndexError:
        return 'Method not allowed', 405

    try:
        users=Users(email)
        return users.get_user(), 200

    except Exception:
        return 'User not found', 404


@bp.route('/user', methods=['PUT'])
def update_user_data():
    try:
        data = request.get_json()
        email = data['email']
        new_data = data['data']

    except IndexError:
        return 'Method not allowed', 405

    
    users=Users(email)
    if users.update_user(new_data) == True:
        return 'True', 200

    else :
        return 'DB error', 404


@bp.route('/user', methods=['DELETE'])
def delete_user():
    try:
        email = request.json('user_email')

    except IndexError:
        return 'Method not allowed', 405

    try:
        user=Users(email)
        user.delete_user()
        
        return 'True', 200
    
    except Exception:
        return 'User not found', 404