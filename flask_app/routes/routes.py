from flask import request
from flask_app.models.models import Artist, AllMusics, Pop, Rap, Trap
from flask_app.get_response import get_response
from flask_app.config import db
import logging


def configure_routes(app):
    @app.route("/")
    def home():
        return "hello"

    @app.route("/home/pop", methods=["GET"])
    def get_allPop():
        try:
            query_pop = Pop.query.all()
            pop_json = [pop.to_json() for pop in query_pop]

            if pop_json:
                return get_response(200, "pop musics", pop_json)
            else:
                return get_response(204, "pop musics", {}, "There's no music here yet.")
        except Exception as e:
            logging.error(e)
            return get_response(417, "error", None, "An error occured.")

    # RAP MUSICS
    @app.route("/home/rap", methods=["GET"])
    def get_allRap():
        try:
            query_rap = Rap.query.all()
            rap_json = [rap.to_json() for rap in query_rap]

            if rap_json:

                return get_response(200, "rap musics", rap_json)
            else:
                return get_response(204, "rap musics", {}, "There's no music here yet.")
        except Exception as e:
            logging.error(e)
            return get_response(417, "rap musics", None, "An error occured")

    # TRAP MUSICS

    @app.route("/home/trap", methods=["GET"])
    def get_allTrap():
        try:
            query_trap = Trap.query.all()
            trap_json = [trap.to_json() for trap in query_trap]

            if trap_json:

                return get_response(200, "rap musics", trap_json)
            else:
                return get_response(204, "rap musics", {}, "There's no music here yet.")
        except Exception as e:
            logging.error(e)
            return get_response(417, "trap musics", {}, "An error occured")

    # POST ARTIST

    @app.route("/home/register-artist", methods=["POST"])
    def postArtist() -> str:
        body = request.get_json()

        try:
            artist = Artist(name=body["name"], genre=body["genre"])
            db.session.add(artist)
            db.session.commit()
            return get_response(201, "artist", artist.to_json(), "Artist registered.")
        except Exception as e:
            logging.error(e)
            return get_response(309, "artist", {}, "Artist already exist.")

    # GET ARTISTS

    @app.route("/home/artists", methods=["GET"])
    def get_allArtists():
        query_artists = Artist.query.all()
        artists_json = [artists.to_json() for artists in query_artists]

        return get_response(200, "artists", artists_json)

    # GET ALL MUSICS

    @app.route("/home/musics", methods=["GET"])
    def get_allMusics():
        query_musics = AllMusics.query.all()
        musics_json = [musics.to_json() for musics in query_musics]

        return get_response(200, "musics", musics_json)

    # POST MUSIC

    @app.route("/home/register-music/genre-<genre>", methods=["POST"])
    def postMusic(genre: str) -> str:
        genre = genre.upper()
        if genre == "TRAP":
            from flask_app.music.musictrap import trapMusic

            return trapMusic()
        elif genre == "POP":
            from flask_app.music.musicpop import popMusic

            return popMusic()
        elif genre == "RAP":
            from flask_app.music.musicrap import rapMusic

            return rapMusic()

    # PUT MUSIC

    # DELETE ARTIST
    @app.route("/home/artists/<artist>", methods=["DELETE"])
    def delete_artist(artist: str):
        artist_obj = Artist.query.filter_by(name=artist).first()
        allmusics = AllMusics.query.filter_by(artist=artist).first()
        try:
            if artist_obj:
                db.session.delete(artist_obj)
                db.session.commit()
                return get_response(
                    200, "artist", artist_obj.to_json(), "Artist deleted."
                )
            elif allmusics:
                db.session.delete(allmusics)
                db.session.commit()
                return get_response(
                    200, "artist", artist_obj.to_json(), "Artist deleted."
                )
            elif artist_obj and allmusics:
                db.session.delete(allmusics)
                db.session.delete(artist_obj)
                db.session.commit()
                return get_response(
                    200, "artist", artist_obj.to_json(), "Artist deleted."
                )

            else:
                return get_response(404, "artist", {}, "Artist not exist.")
        except Exception as e:
            logging.error(e)
            return get_response(404, "artist", {}, "An error occured")

    # DELETE MUSIC
    @app.route("/home/musics/<music>", methods=["DELETE"])
    def delete_music(music: str):
        music_obj = AllMusics.query.filter_by(name=music).first()
        trap = Trap.query.filter_by(name=music).first()
        pop = Pop.query.filter_by(name=music).first()
        rap = Rap.query.filter_by(name=music).first()
        try:
            if music_obj.genre.upper() == "TRAP":
                db.session.delete(trap)
                db.session.delete(music_obj)
                db.session.commit()

                return get_response(200, "music", music_obj.to_json(), "Music deleted.")
            elif music_obj.genre.upper() == "POP":
                db.session.delete(pop)
                db.session.delete(music_obj)
                db.session.commit()

                return get_response(200, "music", music_obj.to_json(), "Music deleted.")
            elif music_obj.genre.upper() == "RAP":
                db.session.delete(rap)
                db.session.delete(music_obj)
                db.session.commit()

                return get_response(200, "music", music_obj.to_json(), "Music deleted.")
            else:

                return get_response(404, "music", {}, "This music not exist.")
        except Exception as e:
            logging.error(e)
            return get_response(417, "error", {}, "Error to delete.")

    @app.route("/home/edit/<music_or_artist>/<ID>", methods=["PUT"])
    def edit_music_or_artist(music_or_artist, ID):
        all_musics = AllMusics.query.filter_by(id=ID).first()
        body = request.get_json()
        if music_or_artist.upper() == "MUSIC":
            try:
                if "name" and "artist" and "genre" in body:
                    all_musics.name = body["name"]
                    all_musics.artist = body["artist"]
                    all_musics.genre = body["genre"]
                    db.session.add(all_musics)
                    db.session.commit()

                    return get_response(
                        200, "music", all_musics.to_json(), "Music edited"
                    )
            except Exception as e:
                logging.error(e)
                return get_response(409, "error", {}, "Same credentials.")
        elif music_or_artist.upper() == "ARTIST":
            try:
                if "name" and "genre" in body:
                    artist = Artist.query.filter_by(id=ID).first()
                    artist.name = body["name"]
                    artist.genre = body["genre"]
                    db.session.add(artist)
                    db.session.commit()
                else:
                    return {"error": "name, genre or artist is missing."}
            except Exception as e:
                logging.error(e)
                return get_response(417, "error", {}, "Error to edit it.")
