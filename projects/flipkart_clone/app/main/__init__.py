from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.main.routes.user import user


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    db.init_app(app)

    app.register_blueprint(user, url_prefix='/user')

    return app
