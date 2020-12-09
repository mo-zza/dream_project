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
        report = Report()
        report.report_vio(email, title, report_type, content, datetime)

        return {}, 200
    except:
        return "token error", 500

@bp.route('/report', methods=['GET'])
def one_report():
    try:
        report_index = request.args.get('index')

    except IndexError:
        
        return { 'data' : { 'message' : 'Method not allowed' } }, 405

    try:
        report = Report()
        report_info = report.get_report(report_index)

        return { 'data' : report_info }, 200
    
    except:
        return { 'data' : { 'message' : 'Report Not Found'} }, 404
