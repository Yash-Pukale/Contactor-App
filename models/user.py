from models import db
from utils import dictify_document
import datetime, uuid
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Document):
    full_name = db.StringField(max_length=150)
    username = db.StringField(max_length=150)
    email = db.StringField(max_length=150)
    password = db.StringField(max_length=None, min_length=None)
    phone = db.StringField(max_length=None, min_length=None)
    created_at = db.DateTimeField()
    refresh_token = db.StringField(max_length=None, min_length=None)
    refresh_token_expiry = db.DateTimeField()
    last_login = db.DateTimeField()
    extra_details = db.DictField()
