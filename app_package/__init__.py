""" The folder 'app_package' contains __init__ which says its a package. We also tell 
Flask to read the config we made for the secret key. """

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This tells flask what the starting point is 
app = Flask(__name__)
app.config.from_object(Config)

# Initialise the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Routes are the different URL's that the application implements. It is not at the top 
# because it is called from app. Models is where we designed our database
from app_package import routes, models  # noqa: E402, F401