import json
from flask import Response


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")