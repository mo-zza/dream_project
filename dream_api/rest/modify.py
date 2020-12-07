from flask import request

from dream_api.rest import bp
from dream_api.use_case.modify import Modify

@bp.route('/modify', methods=['PUT'])
def update_modify():
    try:
        req_data = request.get_json()

        report_index = req_data['index']
        report_status = req_data['status']
    
    except IndexError:

        return 'Method not allowed', 405

    if Modify(report_index, report_status) == True:

        return {}, 200
    else:
        return "There have not report", 404
