from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from models.models import *
from get_response import get_response
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)


@app.route('/home/')
def home():
    return "hello"


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
        from music.musictrap import trapMusic
        return trapMusic()
    elif genre == "POP":
        from music.musicpop import popMusic
        return popMusic()
    elif genre == "RAP":
        from music.musicrap import rapMusic
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
@app.route('/home/musics/<music>', methods=["DELETE"])
def deleteMusic(music):
    music_obj = AllMusics.query.filter_by(name=music).first()
    trap = Trap.query.filter_by(name=music).first()
    pop = Pop.query.filter_by(name=music).first()
    rap = Rap.query.filter_by(name=music).first()
    try:
        if music_obj.genre == "Trap":
            db.session.delete(music_obj)
            db.session.delete(trap)
            db.session.commit()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        elif music_obj.genre.upper() == "POP":
            db.session.delete(music_obj)
            db.session.delete(pop)
            db.session.commit()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        elif music_obj.genre.upper() == "RAP":
            db.session.delete(music_obj)
            db.session.delete(rap)
            db.session.commit()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        else:

            return get_response(404, "music", {}, "This music not exist.")
    except Exception as e:
        print(e)
        return get_response(417, "error", {}, "Error to delete.")


if __name__ == '__main__':
    app.run(debug=True)
