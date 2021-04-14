from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config, MailConfig
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Silahkan login dulu untuk mengakses halaman'
app.config.from_object(MailConfig)
mail = Mail(app)

# import module views yang berisi fungsi CRUD
from app.models import User
from app import views

""" import module user dari folder app/user 
    yang berisi tungsi-fungsi yang berhubungan dengan kebutuhan user"""
from app.user_controller import user_controller
from app.password_reset import password_reset

@login_manager.user_loader
def load_user(id):
    """ Fungsi ini di jalankan untuk menyimpan cookies atau session User 
        agar informasi login user tersimpan dalam LocalStorage import User model dari app/models.py
        params:
           id(int): id user  
        return:
            user(object): object user
        """
    return User.query.get(int(id))
