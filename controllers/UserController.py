from math import log
from flask import request

from flask_sqlalchemy import SQLAlchemy
from models.Factories import Factories

from repositories.FactoriesRepository import FactoriesRepository

db = SQLAlchemy()

def index():
    factories = FactoriesRepository().get()
    
    return {
        'data': '123',
        'factories': factories,
    }