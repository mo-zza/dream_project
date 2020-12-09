from flask import request

from dream_api.rest import bp

@bp.route('/health', methods=['GET'])
def health_check():
    return {}, 200