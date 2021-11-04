from flask import request
from settings import db
from get_response import get_response
from models.models import Rap, AllMusics, Artist


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
