import json
from typing import Optional

from fastapi import APIRouter

import datetime
from mongoengine import Document, StringField, IntField, DateTimeField
from pydantic import BaseModel, SecretStr, Field


class UserModel(BaseModel):
    name: Optional[str] = Field(None, description="Name of the user")
    avatar: Optional[str] = Field(None, description="User gravatar url for avatar")
    email: str = Field(...,  description="User email")
    password: SecretStr = Field(..., description="User password")


class User(Document):
    name = StringField(max_length=100)
    avatar = StringField(default="")
    email = StringField(max_length=100, required=True)
    password = StringField(max_length=100, required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)


# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/api/user",
    tags=['User'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


@router.get("/")
async def get_all_user():
    return json.loads(User.objects().to_json())


@router.get("/{user_id}")
async def get_user(user_id: str):
    return json.loads(User(id=user_id).to_json())

