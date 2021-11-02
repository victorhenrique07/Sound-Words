from flask import Flask, Response
import json

app = Flask(__name__)


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
