""" Creating our database here (schema). The primary key is the ID, and the email and 
usernames are unique values. The passwords are not directly stored in the databse, but 
instead the hashes are which is a security best practice. db.relationship initliases the
posts field in Users. This is a high level view.

The posts database has a foreign key which links the user_id to the id found in the 
users database. This links the two."""

from app_package import db 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Useful for debugging, will return the username.

        Returns:
            string: Username of the user
        """
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)