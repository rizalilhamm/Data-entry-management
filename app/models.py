from flask_login import UserMixin
from app import db
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.title
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    is_editor = db.Column(db.Boolean, default=False)
    about = db.Column(db.String(140))

    def __repr__(self):
        return self.name
