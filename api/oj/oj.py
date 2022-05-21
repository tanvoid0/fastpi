from api.model_lib import *
from api.user.user import UserSchema


class OJModel(BaseModel):
    title: str
    icon: Optional[str]
    progress: Optional[str]
    url: Optional[str]


class OJ(Document):
    title = StringField()
    icon = StringField(required=False)
    progress = StringField(required=False)
    url = StringField(required=False)
    user = ReferenceField(UserSchema)

