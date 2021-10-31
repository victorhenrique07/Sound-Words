from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root:94082@localhost/Genius_API'
db = SQLAlchemy(app)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    genre = db.Column(db.String(25), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "name": self.name, "genre": self.genre}


class Pop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}


class Rap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}


class Trap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), unique=False, nullable=False)
    name = db.Column(db.String(30), unique=False, nullable=False)

    def to_json(self):
        return {"ID": self.id, "artist": self.artist, "name": self.name}


# HOME

@app.route('/home', methods=["GET"])
def home():
    return {'hello': 'world'}


# POP MUSICS

@app.route('/home/pop', methods=["GET"])
def get_allPop():
    try:
        query_pop = Pop.query.all()
        pop_json = [pop.to_json() for pop in query_pop]

        return get_response(200, "pop musics", pop_json)
    except Exception as e:
        print(e)
        return get_response(404, "pop musics", {}, "There's no music here yet.")


# RAP MUSICS

def get_allRap():
    try:
        query_rap = Rap.query.all()
        pop_json = [pop.to_json() for pop in query_rap]

        return get_response(200, "pop musics", pop_json)
    except Exception as e:
        print(e)
        return get_response(404, "pop musics", {}, "There's no music here yet.")


# TRAP MUSICS

@app.route('/home/trap', methods=["GET"])
def get_allTrap():
    try:
        query_trap = Trap.query.all()
        trap_json = [trap.to_json() for trap in query_trap]

        return get_response(200, "trap musics", trap_json)
    except Exception as e:
        print(e)
        return get_response(404, "trap musics", {}, "There's no music here yet")


# POST ARTIST

@app.route('/home/register-artist', methods=["POST"])
def postArtist():
    body = request.get_json()

    try:
        artist = Artist(name=body["Name"], genre=body["Genre"])
        db.session.add(artist)
        db.session.commit()
        return get_response(201, "artist", artist.to_json(), "Artist registered.")
    except Exception as e:
        print(e)
        return get_response(309, "artist", {}, "Artist already exist.")


# GET ARTISTS

@app.route('/home/artists', methods=["GET"])
def get_allArtists():
    query_artists = Artist.query.all()
    artists_json = [artists.to_json() for artists in query_artists]

    return get_response(200, "artists", artists_json)


# POST MUSIC

@app.route('/home/register-music/genre-<genre>', methods=["POST"])
def postMusic(genre):
    genre = genre.upper()
    if genre == "TRAP":
        return trapMusic()
    elif genre == "POP":
        return popMusic()
    elif genre == "RAP":
        return rapMusic()


# PUT MUSIC

# DELETE ARTIST

# DELETE MUSIC


def popMusic():
    body = request.get_json()
    try:
        pop = Pop(artist=body["artist"], name=body["name"])
        # validating if the artist exists.
        artists = Artist.query.filter(Artist.name == body["artist"]).one()
        pop_music = Pop.query.filter(Pop.name == body["name"]).first()
        if pop_music and artists:
            return get_response(309, "music", {}, "Music already exist.")
        else:
            db.session.add(pop)
            db.session.commit()
            return get_response(201, "music", pop.to_json(), "Music registered.")

    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Artist not exist.")


def rapMusic():
    body = request.get_json()
    try:
        rap = Rap(artist=body["artist"], name=body["name"])
        db.session.add(rap)
        db.session.commit()
        return get_response(201, "music", rap.to_json(), "Music registered.")
    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Music already exist.")


def trapMusic():
    body = request.get_json()
    try:
        trap = Trap(artist=body["artist"], name=body["name"])
        db.session.add(trap)
        db.session.commit()
        return get_response(201, "music", trap.to_json(), "Music registered.")
    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Music already exist.")


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
