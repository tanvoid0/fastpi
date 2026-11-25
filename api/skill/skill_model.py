from api.model_lib import *
from api.user.user_model import UserSchema


class SkillModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[float]
    description: Optional[str]


class LanguageModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[float]
    description: Optional[str]


class FrameworkModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[float]
    description: Optional[str]
    language: Optional[str]


class PlatformModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[float]
    description: Optional[str]
    frameworks: Optional[list]


class Skill(Document):
    title = StringField(unique=True)
    image = StringField(required=False)
    fluency = FloatField(required=False)
    description = StringField(default="")
    user = ReferenceField(UserSchema)


class Language(Document):
    title = StringField(unique=True)
    image = StringField(required=False)
    fluency = FloatField(required=False)
    description = StringField(default="")
    user = ReferenceField(UserSchema)


class Framework(Document):
    title = StringField(unique=True)
    image = StringField(required=False)
    fluency = FloatField(required=False)
    description = StringField(default="")
    language = StringField(required=False)
    user = ReferenceField(UserSchema)


class Platform(Document):
    title = StringField(unique=True)
    image = StringField(required=False)
    fluency = FloatField(required=False)
    description = StringField(default="")
    frameworks = ListField(StringField(required=False))
    user = ReferenceField(UserSchema)
