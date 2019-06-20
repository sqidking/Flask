from datetime import datetime
from app import db


# User inherits from db.Model ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # db.relationship defines relationship and is put on the "One" of a "One to Many"
    # Backref argument defines the name of a field that will be added to the objects
    # of the "many" class that points back to the "one" object
    # allows you to use commands such as user.posts to find a users posts

    # This defines what to print when an instance of this class is called directly
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # ^ SQLAlchemy uses lowercase and snake case for database table names

    def __repr__(self):
        return '<Post {}>'.format(self.body)