
import os 
from sqlalchemy import create_engine
import urllib 

class Config(object):
    SECRET_KEY = 'DALE_LEON'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1/bdidgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    