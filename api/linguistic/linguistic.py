from api.model_lib import *
from api.user.user import UserSchema


class LinguisticModel(BaseModel):
    title: str
    image: Optional[str]
    fluency: Optional[str]


class Linguistic(Document):
    title = StringField()
    image = StringField(required=False)
    fluency = StringField(required=False)
    user = ReferenceField(UserSchema)

