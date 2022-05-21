from api.model_lib import *
from api.user.user import UserSchema


class HobbyModel(BaseModel):
    title: str
    icon: Optional[str]


class Hobby(Document):
    title = StringField()
    icon = StringField(required=False)
    user = ReferenceField(UserSchema)

