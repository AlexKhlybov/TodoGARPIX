from os.path import dirname, join

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from todo.config import config
from todo.models import db
from todo.resources import init_api

migrate = Migrate()


def create_app(config_name):
    dotenv_path = join(dirname(__file__), ".env")
    var_env = load_dotenv(dotenv_path)

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    init_api(app)

    if not config_name == "testing":
        migrate.init_app(app, db)
    else:
        with app.app_context():
            db.create_all()
    return app
