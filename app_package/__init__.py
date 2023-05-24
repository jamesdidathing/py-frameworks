""" The folder 'app_package' contains __init__ which says its a package. We also tell 
Flask to read the config we made for the secret key. """

from flask import Flask
from config import Config

# This tells flask what the starting point is 
app = Flask(__name__)
app.config.from_object(Config)

# Routes are the different URL's that the application implements. It is not at the top 
# because it is called from app
from app_package import routes  # noqa: E402, F401