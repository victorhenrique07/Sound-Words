from flask import request
from flask_app.get_response import get_response
from flask_app.models.models import *


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
            rap.save()
            allmusics.save()

            return get_response(201, "music", rap.to_json(), "Music registered.")

    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Artist not exist.")
