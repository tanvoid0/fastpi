from api.model_lib import *
from api.user.user import UserSchema


class LinguisticModel(BaseModel):
    title: str
    icon: Optional[str]
    fluency: Optional[str]


class Linguistic(Document):
    title = StringField()
    icon = StringField(required=False)
    fluency = StringField(required=False)
    user = ReferenceField(UserSchema)

