from flask import request
from dream_api.rest import bp
from dream_api.use_case.report import Report
# from dream_api.object.req_object import req

@bp.route('/user', methods=['POST'])
def create_user():
    try:
        req_data = request.get_json()

        email = req_data['email']
        title = req_data['title']
        report_type = req_data['type']
        content = req_data['content']
        datetime = req_data['datetime']
    
    except IndexError:

        return 'Method not allowed', 405

    report = Report(email)
    create_token = report.report_vio(title, report_type, content, datetime)
    if create_token == True:
        return {}, 200
    else:
        return create_token, 500