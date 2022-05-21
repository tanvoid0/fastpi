from api.model_lib import *
from api.user.user import UserSchema


class SkillModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[float]
    description: Optional[str]


class LanguageModel(SkillModel):
    pass


class FrameworkModel(SkillModel):
    language: Optional[str]


class PlatformModel(SkillModel):
    frameworks: Optional[list]


class Skill(Document):
    title = StringField(unique=True)
    image = StringField(required=False)
    fluency = FloatField(required=False)
    description = StringField(default="")
    user = ReferenceField(UserSchema)

    meta = {'allow_inheritance': True}


class Language(Skill):
    pass


class Framework(Skill):
    language = ReferenceField(Language, required=False, unique=False)


class Platform(Skill):
    frameworks = ListField(ReferenceField(Framework, required=False, unique=False))

