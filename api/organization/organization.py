from api.model_lib import *

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
    institution: StringField(max_length=100, required=False)
    address: StringField(required=False)
    timeline: StringField(required=False)
    description: StringField(required=False)
    activities: StringField(required=False)
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
