from flask import request
from flask_app.get_response import get_response
from flask_app.models.models import Trap, AllMusics
from flask_app.config import db


def trapMusic():
    body = request.get_json()
    try:

        trap = Trap(
            artist=body["artist"], name=body["name"]
        )
        allmusics = AllMusics(
            artist=body["artist"], name=body["name"], genre="Trap"
        )
        trap_music = Trap.query.filter_by(name=body["name"]).first()
        if trap_music is not None:
            return get_response(
                309, "music", {}, "Music already exist."
            )
        else:
            db.session.add(trap)
            db.session.add(allmusics)
            db.session.commit()

            return get_response(
                201, "music", trap.to_json(), "Music registered."
            )

    except Exception as e:
        print(e)
        return get_response(
            417, "music", {}, "Artist not exist."
        )
