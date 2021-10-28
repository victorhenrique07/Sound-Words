from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root:94082@localhost/Genius_API'
db = SQLAlchemy(app)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    genre = db.Column(db.String(25), unique=False, nullable=False)


class Pop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)


class Rap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)


class Trap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)


@app.route('/home', methods=["GET"])
def home():
    return {'hello': 'world'}


@app.route('/home/register')
def teste():
    ...


if __name__ == '__main__':
    app.run(debug=True)
