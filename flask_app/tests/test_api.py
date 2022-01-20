import json

from flask import Flask
from flask_app.routes.routes import configure_routes
from dotenv import dotenv_values
from flask_app.config import db

env = dotenv_values(".env")

DATABASE_URI = env.get("DATABASE_URI")


def test_server_is_running():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_endpoint_post_home_register_artist_is_ok():
    app = Flask(__name__)
    configure_routes(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/register-artist'
    data = {
        "name": "Duzz",
        "genre": "Trap"
    }

    response = client.post(url, json=data)
    assert response.status_code == 201 or response.status_code == 500


