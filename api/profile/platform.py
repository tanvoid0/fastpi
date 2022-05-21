from typing import Optional

from mongoengine import DynamicDocument, StringField, ListField
from pydantic import BaseModel


class PlatformModel(BaseModel):
    name: str
    stacks: Optional[list]


class Platform(DynamicDocument):
    name = StringField()
    stacks = ListField()


