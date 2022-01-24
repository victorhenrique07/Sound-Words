from flask import request
from flask_app.get_response import get_response
from flask_app.models.models import Rap, AllMusics
from flask_app.config import db
import logging


def rapMusic():
    body = request.get_json()
    try:
        rap_music = Rap.query.filter(Rap.name == body["name"]).first()
        rap = Rap(
            artist=body["artist"],
            name=body["name"])
        allmusics = AllMusics(
            name=body["name"],
            artist=body["artist"],
            genre="Rap")

        if rap_music:
            return get_response(
                309, "music", {}, "Music already exist."
            )
        else:
            db.session.add(rap)
            db.session.add(allmusics)
            db.session.commit()

            return get_response(
                201, "music", rap.to_json(), "Music registered."
            )

    except Exception as e:
        logging.error(e)
        return get_response(
            309, "music", {}, "Artist not exist."
        )
