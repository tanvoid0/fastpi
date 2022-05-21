from typing import Optional

from mongoengine import DynamicDocument, StringField, ListField
from pydantic import BaseModel


class ProjectModel(BaseModel):
    title: str
    images: Optional[list[str]]
    description: Optional[str]
    keyword: Optional[list]
    url: Optional[str]


class Project(DynamicDocument):
    title = StringField()
    images = ListField()
    description = StringField()
    keyword = ListField()
    url = StringField()
