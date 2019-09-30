from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite3'
db = SQLAlchemy(app)

from app import routes
