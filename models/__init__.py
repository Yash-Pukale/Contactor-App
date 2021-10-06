from flask_mongoengine import MongoEngine

db = MongoEngine()

from .user import User
