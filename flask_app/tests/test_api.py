from flask import Flask
from flask_app.routes.routes import configure_routes


def test_server_is_running():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200
    