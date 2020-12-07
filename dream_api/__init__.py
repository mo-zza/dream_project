from flask import Blueprint
from dream_api.shared.mongo import MongoDB
from dream_api.shared.line_blockchain import LineBlockchain

db=MongoDB()
blockchain=LineBlockchain()

bp = Blueprint('/', __name__)

from dream_api.rest import user, report, modify, health_check