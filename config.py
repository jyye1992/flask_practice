import os

basedir = os.path.abspath(os.path.dirname(__file__))

FLASK_DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///./tmp/test.db"

SQLALCHEMY_TRACK_MODIFICATIONS = False