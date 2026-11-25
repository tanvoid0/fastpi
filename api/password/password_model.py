from api.model_lib import *
from api.user.user_model import UserSchema


class PasswordType(str, Enum):
    PASSWORD = "PASSWORD"
    ID = "ID"
    NOTE = "NOTE"
    BANKING = "BANKING"
    TOKEN = "TOKEN"


class PasswordModel(BaseModel):
    website: Optional[str] = Field()
    name: str = Field()
    username: str = Field()
    password: str = Field()
    category: Optional[str] = Field()
    note: Optional[str] = Field()
    type: Optional[PasswordType] = Field(PasswordType.PASSWORD)


class Password(Document):
    website = StringField()
    name = StringField()
    username = StringField()
    password = StringField()
    category = StringField()
    note = StringField()
    type = StringField()
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(UserSchema)

