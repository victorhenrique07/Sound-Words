from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    app.db = db


class BasicMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Artist(BasicMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    genre = db.Column(db.String(25), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "name": self.name, "genre": self.genre}

