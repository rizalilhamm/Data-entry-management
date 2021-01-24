import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = 'postgres://ieewmsajiwstkj:cb79b12c40acda7f08b8b3fde724d88e0817bc32b79fa59ff01f42197c6f9c2a@ec2-174-129-199-54.compute-1.amazonaws.com:5432/deojl748tr6841'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')