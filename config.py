""" Flask and some extensions use the value of the secret key as a cryptographic key to 
generate signatures or tokens. The first terms (SECRET_KEY) looks for an environment 
variable of the same name. The idea is that a value sourced from an environment variable
is preferred, but if the environment does not define the variable, then the hardcoded 
string is used instead as a default. For this case, security is low. """

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'