import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    heroku_db = 'postgres://cxvgwzcndxklsb:6f2faee447fe6b76854f17391a5fdcea0ec2052be4ecc540bfad5c4f918cc2df@ec2-34-201-248-246.compute-1.amazonaws.com:5432/d9frgf90qs3occ'
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ini-rahasia'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or heroku_db
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or True