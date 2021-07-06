from flask import Flask

from todo.config import config
from todo.models import db
from todo.resources import init_api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    init_api(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()
    return app
