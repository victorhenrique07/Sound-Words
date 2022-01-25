from flask import Flask
from flask_app.config import db
from flask_app.routes.routes import configure_routes
from flask_migrate import Migrate
import os

DATABASE_URI = os.getenv("DATABASE_URI")

app = Flask(__name__)

configure_routes(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sjjpjogjfvelel" \
                                        ":ef4a9f37828c1fb02ebb6bfc1c1b7fbc9c4f5e9befe7ca6644f8d1c8ca3e51d8@ec2-3-216" \
                                        "-113-109.compute-1.amazonaws.com:5432/d5rcanjcc13umr "
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
