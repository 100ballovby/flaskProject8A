import os
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = /Users/demidraksin/PycharmProjects/flaskProject8A/config.py


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'try-to-guess'

