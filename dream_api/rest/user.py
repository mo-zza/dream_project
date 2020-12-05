from flask import request
from dream_api.rest import bp
from dream_api.use_case.user import Users
# from dream_api.object.req_object import req


@bp.route('/user', methods=['POST'])
def create_user():
    try:
        req_data = request.get_json()

        email=req_data['email']
        password=req_data['password']
        name=req_data['name']
        birth=req_data['birth']
        phone=req_data['phone']
        school=req_data['school']
        address=req_data['address']

    
    except IndexError:

        return 'Method not allowed', 405

    users=Users(email)

    if users.create_user(name, password, birth, phone, school, address) == True:
        return  {}, 200
    else:
        return 'User already exist', 400

        

@bp.route('/user', methods=['GET'])
def search_user():
    try:
        data = request.get_json()
        email = data['email']

    except IndexError:
        return 'Method not allowed', 405

    
    users=Users(email)
    user_info = users.get_user()

    if user_info != False:

        user_info = user_info[0]
        del(user_info['_id'])

        return user_info, 200
    else:
        
        return 'User not found', 404