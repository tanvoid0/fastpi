from api.model_lib import *
from api.user.user import UserSchema


class LanguageModel(BaseModel):
    title: str
    icon: Optional[str]
    fluency: Optional[str]


class Language(Document):
    title = StringField()
    icon = StringField(required=False)
    fluency = StringField(required=False)
    user = ReferenceField(UserSchema)

