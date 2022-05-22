from api.model_lib import *


class UserModel(BaseModel):
    name: Optional[str]
    fullName: Optional[str]
    avatar: Optional[str]
    coverImg: Optional[str]
    yob: Optional[str]
    address: Optional[str]
    degree: Optional[str]
    phone: Optional[str]
    title: Optional[str]
    whatIDo: Optional[str]
    about: Optional[str]
    aboutDetailed: Optional[str]
    username: Optional[str]
    email: str
    publicEmail: Optional[str]
    password: Optional[str]


class UserSchema(Document):
    name = StringField()
    fullName = StringField(required=False)
    avatar = StringField(required=False)
    coverImg = StringField(required=False)
    yob = StringField(required=False)
    address = StringField(required=False)
    degree = StringField(required=False)
    phone = StringField(required=False)
    title = StringField(required=False)
    whatIDo = StringField(required=False)
    about = StringField(required=False)
    aboutDetailed = StringField(required=False)
    username = StringField(required=False)
    email = StringField(max_length=100, required=True, unique=True)
    publicEmail = StringField()
    password = StringField(required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'collection': 'user'}

