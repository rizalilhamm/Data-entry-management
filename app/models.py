import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt
from app import db, app
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.title
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # berfungsi untuk menyimpan ID user dan menjadikannya kunci utama
    name = db.Column(db.String(20), index=True, nullable=False, unique=True) # menyimpan nama user
    email = db.Column(db.String(20), nullable=False, unique=True) # menyimpan email user, tidak boleh kosong dan harus unik
    password = db.Column(db.String(100)) # menyimpan password user
    is_admin = db.Column(db.Boolean, default=False) # menyimpan status user sebagai admin, editor atau user biasa
    is_editor = db.Column(db.Boolean, default=False)
    about = db.Column(db.String(140)) # user dapat menambahkan bio atau mengkosongkannya
    
    def get_reset_token(self):
        # Membuat tanda tangan digital
        token = jwt.encode({
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }, os.getenv('SECRET_KEY'), algorithm="HS256")
        return token
    
    @staticmethod
    def verify_reset_token(token):
        try:    
            # periksa tanda tangan digital
            signature = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        except:
            return None
        return User.query.filter_by(email=signature['email']).first()

    def hash_password(self):
        self.password = generate_password_hash(self.password, method='sha256')
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.name
