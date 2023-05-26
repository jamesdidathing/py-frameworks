""" This is the place where Flask itself puts certain configuration values and also
where extensions can put their configuration values. """

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Best practice is to set configuration from environmental variables and then have
# fallback value.
class Config(object):

    # Cryptographic key for signatures and tokens. Atm, it is simple
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # This would send a signal to the application everytime the database changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
