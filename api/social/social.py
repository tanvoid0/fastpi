from api.model_lib import *
from api.user.user import UserSchema


class SocialModel(BaseModel):
    name: str
    url: str
    icon: Optional[str]


class Social(Document):
    name = StringField()
    url = StringField()
    icon = StringField(required=False)
    user = ReferenceField(UserSchema)
