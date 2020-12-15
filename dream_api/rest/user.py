from flask import request
from dream_api.rest import bp
from dream_api.use_case.user import Users
# from dream_api.object.req_object import req


@bp.route('/join', methods=['POST'])
def create_user():
    try:
        req_data = request.get_json()

        email=req_data['email']
        password=req_data['password']
        name=req_data['name']
        school=req_data['school']
        phone=req_data['phone']
        address=req_data['address']
        detail_address = req_data['detail_address']
        birth=req_data['birth']

    
    except IndexError:

        return { 'data' : { 'message' : 'Method not allowed' } }, 405

    users=Users(email)

    if users.create_user(name, password, birth, phone, school, address, detail_address) == True:
        return  {}, 201
    else:
        return 'Server Error', 500

@bp.route('/login', methods=['POST'])
def search_user():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

    except IndexError:
        return { 'data' : { 'message' : 'Method not allowed' } }, 405

    
    users=Users(email)
    user_info = users.get_user(password)

    if user_info == 'User':

        return { 'data' : { 'message' : 'Usser not found' } }, 404
        
    elif user_info == 'Password':
        
        return { 'code' : 40100, 'data' : { 'message' : 'Invalied passwrod'}}, 401

    else:
        return { 'data' : { 'token' : user_info} }, 200

@bp.route('/email-status', methods=['GET'])
def email_check():
    try:
        email = request.args.get('email')

    except IndexError:
        return { 'data' : { 'message' : 'Method not allowed' } }, 405

    users=Users(email)
    user_info = users.check_user()

    if user_info == None:

        return { 'data' : { 'duplicate' : 'true'}}, 200
    else:

        return { 'data' : { 'duplicate' : 'false'}}, 400