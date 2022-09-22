from . import db
from flask_login import UserMixin


class Profile(UserMixin, db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(64), unique=True)
    bio = db.Column(db.Text, default='i love one profile')
    social_links = db.relationship('Comment', backref='post')
    def __repr__(self):
        return '<Profile %r>'% self.name

class Link(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
        return '<Link %r>' % self.name
