import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ini-rahasia'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgres://ubuiqvveydpbaj:91fdc5b92df19a8cf3cbfefca133c11c8532d54a5fd8d935dd2336e3bded5d28@ec2-52-45-140-104.compute-1.amazonaws.com:5432/d45ac0kk3kpa72'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or True