from flask import request, Response
import json
from get_response import get_response
from settings import db
from models.models import Pop, AllMusics, Artist


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
