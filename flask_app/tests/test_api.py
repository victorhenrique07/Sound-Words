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


def test_endpoint_post_home_register_artist_is_posting():
    app = Flask(__name__)
    configure_routes(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/register-artist'
    data = {
        "name": "Eminem",
        "genre": "Rap"
    }

    response = client.post(url, json=data)
    assert response.status_code == 201 or response.status_code == 309


def test_if_endpoint_home_pop_is_showing_all_pop_musics():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/pop'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 204


def test_if_endpoint_home_rap_is_showing_all_rap_musics():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/rap'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 204


def test_if_endpoint_home_trap_is_showing_all_trap_musics():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/trap'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 204


def test_if_endpoint_home_artists_is_showing_all_artists():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/artists'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 204


def test_if_endpoint_home_musics_is_showing_all_musics():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/musics'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 204


def test_if_endpoint_home_register_music_is_posting():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/register-music/genre-trap'
    data = {
        'artist': 'Duzz',
        'name': 'Hayabusa'
    }

    response = client.post(url, json=data)
    assert response.status_code == 201 or response.status_code == 204


def test_if_endpoint_home_artist_is_deleting():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/artists/Eminem'

    response = client.delete(url)
    assert response.status_code == 200


def test_if_endpoint_home_musics_is_deleting():
    app = Flask(__name__)
    configure_routes(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    client = app.test_client()
    url = '/home/musics/Superman'

    response = client.delete(url)
    assert response.status_code == 200
