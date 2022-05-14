import datetime

from app import app, json, status, BaseModel
from mongoengine import Document, StringField, IntField, DateTimeField


class UserModel(BaseModel):
    name: str
    avatar: str
    email: str
    password: str
    date_modified: datetime.datetime


class UserSchema(Document):
    name = StringField(max_length=100)
    avatar = StringField(default="")
    email = StringField(max_length=100, required=True)
    password = StringField(max_length=100, required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
