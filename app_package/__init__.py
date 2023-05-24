""" The folder 'app_package' contains __init__ which says its a package"""


from flask import Flask

# This tells flask what the starting point is 
app = Flask(__name__)

# Routes are the different URL's that the application implements. It is not at the top 
# because it is called from app
from app_package import routes