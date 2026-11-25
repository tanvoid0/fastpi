from api.model_lib import *
from api.user.user_model import UserSchema


class OrganizationModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")


class AcademicModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")
    graduation: str


class AchievementModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")
    achievement: Optional[str]


class CertificateModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")
    graduation: Optional[str] = Field("")
    url: Optional[str] = Field("")
    certificate: str


class ExperienceModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")
    role: Optional[str]


class VolunteerModel(BaseModel):
    title: str
    logo: Optional[str]
    images: Optional[list]
    institution: str
    address: Optional[str] = Field("")
    timeline: Optional[str] = Field("")
    description: Optional[str] = Field("")
    activities: Optional[str] = Field("")
    role: Optional[str]


class Organization(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution = StringField(max_length=100, required=False)
    address = StringField(required=False)
    timeline = StringField(required=False)
    description = StringField(required=False)
    activities = StringField(required=False)
    user = ReferenceField(UserSchema)

    meta = {'allow_inheritance': True}


class Academic(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution = StringField(max_length=100, required=False)
    address = StringField(required=False)
    timeline = StringField(required=False)
    description = StringField(required=False)
    activities = StringField(required=False)
    user = ReferenceField(UserSchema)
    graduation = StringField(max_length=100, required=True)


class Achievement(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution= StringField(max_length=100, required=False)
    address= StringField(required=False)
    timeline= StringField(required=False)
    description= StringField(required=False)
    activities= StringField(required=False)
    user = ReferenceField(UserSchema)
    achievement = StringField(required=False, default="")


class Certificate(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution= StringField(max_length=100, required=False)
    address= StringField(required=False)
    timeline= StringField(required=False)
    description= StringField(required=False)
    activities= StringField(required=False)
    user = ReferenceField(UserSchema)
    graduation = StringField(max_length=100, required=False)
    url = StringField(required=False)
    certificate = StringField(required=True)


class Experience(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution= StringField(max_length=100, required=False)
    address= StringField(required=False)
    timeline= StringField(required=False)
    description= StringField(required=False)
    activities= StringField(required=False)
    user = ReferenceField(UserSchema)
    role = StringField(required=False, default="")


class Volunteer(Document):
    title = StringField(max_length=100, required=True)
    logo = StringField(required=False)
    images = ListField(required=False)
    institution = StringField(max_length=100, required=False)
    address = StringField(required=False)
    timeline = StringField(required=False)
    description = StringField(required=False)
    activities = StringField(required=False)
    user= ReferenceField(UserSchema)
    role = StringField(required=False, default="")
