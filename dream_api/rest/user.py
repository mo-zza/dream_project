from flask import request
from dream_api.rest import bp
from dream_api.user_case.user import Users
# from dream_api.object.req_object import req


@bp.route('/user', methods=['POST'])
def create_user():
    try:
        email = request.json('user_email')
        name = request.json('name')
        password = request.json('password')
        birth = request.json('birth')
        phone = request.json('phone')
        school = request.json('school')
        address = request.json('address')
    
    except IndexError:
        return 'Method not allowed', 405

    try:
        users=Users(email)
        users.create_user(name, password, birth, phone, school, address)

        return 'True', 200

    except  Exception:
        return 'User not found', 404
        

@bp.route('/user', methods=['GET'])
def search_user():
    try:
        email = request.json('user_email')

    except IndexError:
        return 'Method not allowed', 405

    try:
        users=Users(email)
        return users.check_user(), 200

    except Exception:
        return 'User not found', 404


@bp.route('/user', methods=['PUT'])
def update_user_data():
    try:
        email = request.json('user_email')
        data = request('data')

    except IndexError:
        return 'Method not allowed', 405

    try:
        new_data = data.item
        users=Users(email)
        users.update_user(new_data)

        return 'True', 200

    except Exception:
        return 'User not found', 404


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