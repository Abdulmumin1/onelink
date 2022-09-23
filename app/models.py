from . import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Profile(UserMixin, db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(64), unique=True)
    bio = db.Column(db.Text, default='i love one profile')
    social_links = db.relationship('Link', backref='post')

    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<Profile %r>'% self.name

class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
        return '<Link %r>' % self.name

@login.user_loader
def load_user(user_id):
    return Profile.query.get(user_id)
