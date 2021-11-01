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


class AllMusics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    artist = db.Column(db.String(30), unique=False, nullable=False)
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

        if pop_json:
            return get_response(200, "pop musics", pop_json)
        else:
            return get_response(204, "pop musics", {}, "There's no music here yet.")
    except Exception as e:
        print(e)
        return get_response(417, "error", None, "An error occured.")


# RAP MUSICS
@app.route('/home/rap', methods=["GET"])
def get_allRap():
    try:
        query_rap = Rap.query.all()
        rap_json = [rap.to_json() for rap in query_rap]

        if rap_json:

            return get_response(200, "rap musics", rap_json)
        else:
            return get_response(204, "rap musics", {}, "There's no music here yet.")
    except Exception as e:
        print(e)
        return get_response(417, "rap musics", None, "An error occured")


# TRAP MUSICS

@app.route('/home/trap', methods=["GET"])
def get_allTrap():
    try:
        query_trap = Trap.query.all()
        trap_json = [trap.to_json() for trap in query_trap]

        if trap_json:

            return get_response(200, "rap musics", trap_json)
        else:
            return get_response(204, "rap musics", {}, "There's no music here yet.")
    except Exception as e:
        print(e)
        return get_response(417, "trap musics", {}, "An error occured")


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


# GET ALL MUSICS

@app.route('/home/musics', methods=["GET"])
def get_allMusics():
    query_musics = AllMusics.query.all()
    musics_json = [musics.to_json() for musics in query_musics]

    return get_response(200, "musics", musics_json)


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
@app.route('/home/artists/<artist>', methods=["DELETE"])
def deleteArtist(artist):
    artist_obj = Artist.query.filter_by(name=artist).first()
    allmusics = AllMusics.query.filter_by(artist=artist).first()
    try:
        if Artist.query.filter(Artist.name == artist).first():
            db.session.delete(allmusics)
            db.session.delete(artist_obj)
            db.session.commit()
            return get_response(200, "artist", artist_obj.to_json(), "Artist deleted.")
        else:
            return get_response(404, "artist", {}, "Artist not exist.")
    except Exception as e:
        print(e)
        return get_response(404, "artist", {}, "An error occured")


# DELETE MUSIC
@app.route('/home/musics/<music>', methods=["GET"])
def deleteMusic(music):
    ...


def popMusic():
    body = request.get_json()
    try:
        pop = Pop(artist=body["artist"], name=body["name"])
        allmusics = AllMusics(name=body["name"], artist=body["artist"], genre="Pop")
        # validating if the artist exists.
        artists = Artist.query.filter(Artist.name == body["artist"]).one()
        pop_music = Pop.query.filter(Pop.name == body["name"]).first()
        if pop_music and artists:
            return get_response(309, "music", {}, "Music already exist.")
        else:
            db.session.add(allmusics)
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
        # validating if the artist exists.
        artists = Artist.query.filter(Artist.name == body["artist"]).one()
        rap_music = Rap.query.filter(Rap.name == body["name"]).first()
        allmusics = AllMusics(name=body["name"], artist=body["artist"], genre="Rap")
        if rap_music and artists:
            return get_response(309, "music", {}, "Music already exist.")
        else:
            db.session.add(rap)
            db.session.add(allmusics)
            db.session.commit()
            return get_response(201, "music", rap.to_json(), "Music registered.")

    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Artist not exist.")


def trapMusic():
    body = request.get_json()
    try:
        trap = Trap(artist=body["artist"], name=body["name"])
        allmusics = AllMusics(artist=body["artist"], name=body["name"], genre="Trap")
        # validating if the artist exists.
        artists = Artist.query.filter(Artist.name == body["artist"]).one()
        trap_music = Trap.query.filter(Trap.name == body["name"]).first()
        if trap_music and artists:
            return get_response(309, "music", {}, "Music already exist.")
        else:
            db.session.add(trap)
            db.session.add(allmusics)
            db.session.commit()
            return get_response(201, "music", trap.to_json(), "Music registered.")

    except Exception as e:
        print(e)
        return get_response(417, "music", {}, "Artist not exist.")


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
