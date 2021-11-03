from flask import request, Response
import json
from get_response import get_response
from settings import db
from models.models import Trap, AllMusics, Artist


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
