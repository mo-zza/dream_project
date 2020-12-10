from flask import Flask
from flask import Blueprint
import logging

from config import Config

logging.basicConfig(filename = "../log/dream.log", level = logging.DEBUG)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from dream_api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')