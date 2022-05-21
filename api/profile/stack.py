from typing import Optional

from mongoengine import DynamicDocument, StringField
from pydantic import BaseModel


class StackModel(BaseModel):
    title: str
    skill: Optional[list]


class Stack(DynamicDocument):
    title: StringField()