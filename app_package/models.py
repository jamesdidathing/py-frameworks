""" Creating our database here (schema). The primary key is the ID, and the email and usernames
are unique values. The passwords are not directly stored in the databse, but instead
the hashes are which is a security best practice. """

from app_package import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """Useful for debugging, will return the username.

        Returns:
            string: Username of the user
        """
        return '<User {}>'.format(self.username)
    
