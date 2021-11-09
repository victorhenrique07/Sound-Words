from flask import request
from flask_app.get_response import get_response
from flask_app.models.models import *


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
            pop.save()
            allmusics.save()

            return get_response(201, "music", pop.to_json(), "Music registered.")

    except Exception as e:
        print(e)
        return get_response(309, "music", {}, "Artist not exist.")
