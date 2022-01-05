from flask import Flask
from flask_app.config import db
from flask_app.routes.routes import blue_routes
from dotenv import dotenv_values

env = dotenv_values(".env")

DATABASE_URI = env.get("DATABASE_URI")

app = Flask(__name__)

app.register_blueprint(blue_routes)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.before_first_request
def create_database():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
