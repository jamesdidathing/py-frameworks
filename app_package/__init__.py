""" The folder 'app_package' contains __init__ which says its a package. We also tell 
Flask to read the config we made for the secret key. """

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os


# This tells flask what the starting point is 
app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

# Initialise the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Routes are the different URL's that the application implements. It is not at the top 
# because it is called from app. Models is where we designed our database
from app_package import routes, models, errors  # noqa: E402, F401

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/website.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s "(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Website startup')