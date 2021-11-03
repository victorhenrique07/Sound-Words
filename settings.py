from flask_sqlalchemy import SQLAlchemy
import os
from main import app
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = {os.getenv("DATABASE_URL")}
db = SQLAlchemy(app)