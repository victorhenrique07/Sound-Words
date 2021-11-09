from flask import Flask
from config import Config, db
from routes.routes import blue_routes


def create_app(test=None):
    app = Flask(__name__)
    app.register_blueprint(blue_routes)
    app.config.from_object(Config)

    if test is not None:
        app.config.from_object(test)
        db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
