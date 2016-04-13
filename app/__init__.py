from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from app import views,models