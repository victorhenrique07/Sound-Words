from flask import Flask
from flask_app.config import db
from flask_app.routes.routes import configure_routes
import os

DATABASE_URI = os.getenv("DATABASE_URI")

app = Flask(__name__)

configure_routes(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
