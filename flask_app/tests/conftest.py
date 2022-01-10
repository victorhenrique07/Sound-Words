from pytest import fixture
from flask_app.main import app


@fixture
def client():
    with app.test_client() as client:
        yield client
