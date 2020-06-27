from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('flaskSetting.py')

db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

from . import errors, views, commands

