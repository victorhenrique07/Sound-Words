from soundwords.ext import configuration
from soundwords.ext.database import init_app
from dotenv import dotenv_values
from flask import Flask
from flask_migrate import Migrate

env = dotenv_values(".env")

DATABASE_URL = env.get("DATABASE_URL")


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    configuration.init_app(app)

    init_app(app)

    Migrate(app, app.db)

    return app
