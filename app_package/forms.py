""" Creating a login form using flask-wtf. Flask-wtf is an extension to use forms.
It creates objects for HTML forms such as text fields, buttons, menus. """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    # Username and Password forms, where validators is to check that the field is filled
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')