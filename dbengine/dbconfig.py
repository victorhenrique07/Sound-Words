from flask_sqlalchemy import SQLAlchemy
from main import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root:94082@localhost/Genius_API'
db = SQLAlchemy(app)
