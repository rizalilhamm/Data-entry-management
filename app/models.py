from werkzeug.security import generate_password_hash, check_password_hash
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
    # berfungsi untuk menyimpan ID user dan menjadikannya kunci utama
    id = db.Column(db.Integer, primary_key=True)
    # menyimpan nama user
    name = db.Column(db.String(20), index=True, nullable=False, unique=True)
    # menyimpan email user, tidak boleh kosong dan harus unik
    email = db.Column(db.String(20), nullable=False, unique=True)
    # menyimpan password user
    password = db.Column(db.String(100))
    # menyimpan status user sebagai admin, editor atau user biasa
    is_admin = db.Column(db.Boolean, default=False)
    is_editor = db.Column(db.Boolean, default=False)
    # user dapat menambahkan bio atau mengkosongkannya
    about = db.Column(db.String(140))

    def hash_password(self):
        self.password = generate_password_hash(self.password, method='sha256')
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.name
