from typing import Optional

from mongoengine import DynamicDocument, StringField, ListField, ReferenceField
from pydantic import BaseModel, Field

from api.user.user import UserSchema


class OrganizationModel(BaseModel):
    title: str
    image: Optional[str]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")


class AcademicModel(OrganizationModel):
    graduation: str


class AchievementModel(OrganizationModel):
    achievement: Optional[str]


class CertificateModel(OrganizationModel):
    image: Optional[str] = Field("")
    graduation: Optional[str] = Field("")
    url: Optional[str] = Field("")


class ExperienceModel(OrganizationModel):
    role: Optional[str]


class VolunteerModel(OrganizationModel):
    role: Optional[str]


class Organization(DynamicDocument):
    title = StringField(max_length=100, required=True)
    image = StringField(required=False)
    institution: StringField(max_length=100, required=True)
    address: StringField(required=False, default="")
    timeline: StringField(required=False, default="")
    description: StringField(required=False, default="")
    activities: StringField(required=False, default="")
    user: ReferenceField(UserSchema)

    meta = {'allow_inheritance': True}


class Academic(Organization):
    graduation = StringField(max_length=100, required=True)


class Achievement(Organization):
    achievement = StringField(required=False, default="")


class Certificate(Organization):
    image = StringField(required=False)
    graduation = StringField(max_length=100, required=False)
    url = StringField(required=False)


class Experience(Organization):
    role = StringField(required=False, default="")


class Volunteer(Organization):
    role = StringField(required=False, default="")
