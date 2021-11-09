from flask import request, Blueprint
from ..models.models import Artist, AllMusics, Pop, Rap, Trap
from ..get_response import get_response


blue_routes = Blueprint('routes', __name__)


@blue_routes.route('/home/')
def home():
    return "hello"


@blue_routes.route('/home/pop', methods=["GET"])
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
@blue_routes.route('/home/rap', methods=["GET"])
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

@blue_routes.route('/home/trap', methods=["GET"])
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

@blue_routes.route('/home/register-artist', methods=["POST"])
def postArtist():
    body = request.get_json()

    try:
        artist = Artist(name=body["Name"], genre=body["Genre"])
        artist.save()
        return get_response(201, "artist", artist.to_json(), "Artist registered.")
    except Exception as e:
        print(e)
        return get_response(309, "artist", {}, "Artist already exist.")


# GET ARTISTS

@blue_routes.route('/home/artists', methods=["GET"])
def get_allArtists():
    query_artists = Artist.query.all()
    artists_json = [artists.to_json() for artists in query_artists]

    return get_response(200, "artists", artists_json)


# GET ALL MUSICS

@blue_routes.route('/home/musics', methods=["GET"])
def get_allMusics():
    query_musics = AllMusics.query.all()
    musics_json = [musics.to_json() for musics in query_musics]

    return get_response(200, "musics", musics_json)


# POST MUSIC

@blue_routes.route('/home/register-music/genre-<genre>', methods=["POST"])
def postMusic(genre):
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
@blue_routes.route('/home/artists/<artist>', methods=["DELETE"])
def deleteArtist(artist):
    artist_obj = Artist.query.filter_by(name=artist).first()
    allmusics = AllMusics.query.filter_by(artist=artist).first()
    try:
        if Artist.query.filter(Artist.name == artist).first():
            artist.delete()
            allmusics.delete()
            return get_response(200, "artist", artist_obj.to_json(), "Artist deleted.")
        else:
            return get_response(404, "artist", {}, "Artist not exist.")
    except Exception as e:
        print(e)
        return get_response(404, "artist", {}, "An error occured")


# DELETE MUSIC
@blue_routes.route('/home/musics/<music>', methods=["DELETE"])
def deleteMusic(music):
    music_obj = AllMusics.query.filter_by(name=music).first()
    trap = Trap.query.filter_by(name=music).first()
    pop = Pop.query.filter_by(name=music).first()
    rap = Rap.query.filter_by(name=music).first()
    try:
        if music_obj.genre == "Trap":
            music_obj.delete()
            trap.delete()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        elif music_obj.genre.upper() == "POP":
            music_obj.delete()
            pop.delete()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        elif music_obj.genre.upper() == "RAP":
            rap.delete()
            music_obj.delete()

            return get_response(200, "music", music_obj.to_json(), "Music deleted.")
        else:

            return get_response(404, "music", {}, "This music not exist.")
    except Exception as e:
        print(e)
        return get_response(417, "error", {}, "Error to delete.")
