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
    # stacks: Optional[list[StackModel]]
    # skills: Optional[list]
    # academics: Optional[list[AcademicModel]]
    # certificates: Optional[list[AcademicModel]]
    # achievements: Optional[list[AchievementModel]]
    # experiences: Optional[list[ExperienceModel]]
    avatar: Optional[str]
    email: str
    publicEmail: Optional[str]
    password: str


class UserSchema(Document):
    name = StringField()
    publicEmail = StringField()
    email = StringField(max_length=100, required=True, unique=True)
    password = StringField(required=True)
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
    skills = DictField(required=False)
    socials = DictField(required=False)
    languages = DictField(required=False)
    academics = DictField(required=False)
    achievements = DictField(required=False)
    certificates = DictField(required=False)
    experiences = DictField(required=False)
    hobbies = DictField(required=False)
    ojs = DictField(required=False)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'collection': 'user'}

