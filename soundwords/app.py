from soundwords.ext import configuration, database
from flask import Flask


app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)