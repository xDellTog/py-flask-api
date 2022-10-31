import contextlib
import os
from flask import Flask
from app.controllers import initial, users

def create_app(test_config=None):
    app = Flask(__name__, 
        instance_relative_config=True,
        static_url_path='/static',
        static_folder='static'
    )

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    with contextlib.suppress(OSError):
        os.makedirs(app.instance_path)
    
    app.register_blueprint(initial.bp)
    app.register_blueprint(users.bp)

    return app