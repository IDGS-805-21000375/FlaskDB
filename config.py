import os
from sqlalchemy import create_engine
import urllib

class config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False
   
class DevelopmentConfig(config):
    DEBUF=True
    AQLALCHEMY_DATABASE_URL='mysql+pymysql://admin:root127.0.0.1/bdidgs805'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    