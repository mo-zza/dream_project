from flask import request
from dream_api.rest import bp
from dream_api.use_case.report import Report
# from dream_api.object.req_object import req

@bp.route('/regist', methods=['POST'])
def regist():
    try:
        req_data = request.get_json()

        email = req_data['email']
        title = req_data['title']
        report_type = req_data['type']
        content = req_data['content']
        datetime = req_data['datetime']
    
    except IndexError:

        return 'Method not allowed', 405


    try:
        report = Report(email)
        report.report_vio(title, report_type, content, datetime)

        return {}, 200
    except:
        return "token error", 500
