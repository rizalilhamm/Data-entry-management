from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Silahkan login dulu untuk mengakses halaman'

# import module views yang berisi fungsi CRUD 
from app import views
""" import module user dari folder app/user 
    yang berisi tungsi-fungsi yang berhubungan dengan kebutuhan user"""
from app.user_controller import user_controller


@login_manager.user_loader
def load_user(id):
    """   Fungsi ini di jalankan untuk menyimpan cookies atau session User 
    agar informasi login user tersimpan dalam LocalStorage import User model dari app/models.py  """
    from app.models import User
    return User.query.get(int(id))
