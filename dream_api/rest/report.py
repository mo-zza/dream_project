from flask import request
from dream_api.rest import bp
from dream_api.use_case.report import Report
# from dream_api.object.req_object import req

@bp.route('/regist', methods=['POST'])
def regist():
    try:
        req_data = request.get_json()

        title = req_data['title']
        category = req_data['category']
        content = req_data['report']
        owner = req_data['owner']
    
    except IndexError:

        return 'Method not allowed', 405


    try:
        report = Report()
        report.report_vio(owner, title, category, content)

        return {}, 201
    except:
        return "token error", 500

@bp.route('/report', methods=['GET'])
def get_report():
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

@bp.route('/empathy', methods=['POST'])
def add_empathy():
    try:
        report_index = request.args.get('index')

    except IndexError:

        return{ 'data' : { 'message' : 'Method not allowed' } }, 405

    report = Report()
    empathy_result = report.add_count(report_index, 'empathy')

    if empathy_result == True:

        return {}, 200
    else:

        return { 'data' : { 'message' : 'Not Found' } }, 404

@bp.route('/support', methods=['POST'])
def add_support():
    try:
        report_index = request.args.get('index')

    except IndexError:

        return{ 'data' : { 'message' : 'Method not allowed' } }, 405

    report = Report()
    empathy_result = report.add_count(report_index, 'support')

    if empathy_result == True:

        return {}, 200
    else:
        
        return { 'data' : { 'message' : 'Not Found' } }, 404