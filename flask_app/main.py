from flask import Flask
from flask_app.config import db
from flask_app.routes.routes import configure_routes
from flask_migrate import Migrate
import os

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

configure_routes(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
