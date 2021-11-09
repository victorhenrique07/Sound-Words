from ..config import db


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


class AllMusics(BasicMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    genre = db.Column(db.String(25), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name, "genre": self.genre}


class Pop(BasicMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}


class Rap(BasicMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}


class Trap(BasicMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}