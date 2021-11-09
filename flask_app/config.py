from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

env = dotenv_values(".env")

DATABASE_URL = env.get("DATABASE_URL")


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    PREFIX = "api/vi"


db = SQLAlchemy()