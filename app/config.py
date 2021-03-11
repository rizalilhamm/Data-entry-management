import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ini-rahasia'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgres://ypfwhduleiexbv:072e0b11baaa33481161caee5165711eaadddd9fa0399fa7698134d33ba414fc@ec2-52-7-115-250.compute-1.amazonaws.com:5432/d4rmigt1rhqqub'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or True