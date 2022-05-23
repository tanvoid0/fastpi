from api.lib import *

from api.hobby.hobby import Hobby
from api.linguistic.linguistic import Linguistic
from api.oj.oj import OJ
from api.organization.organization import Academic, Achievement, Certificate, Organization, Experience
from api.skill.skill import Skill, Language, Framework, Platform
from api.social.social import Social
from api.user.user import UserSchema, UserModel

router = APIRouter(
    prefix="/api/user",
    tags=['User'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


@router.get("/")
async def get_all_user():
    return json.loads(UserSchema.objects().to_json())


@router.get("/{username}")
def get_portfolio(username: str):
    # uid = get_id_from_jwt(token)
    user = UserSchema.objects(username=username).get()
    uid = str(user.pk)
    user = json.loads(user.to_json())

    extra_sources = {
        'hobbies': json.loads(Hobby.objects(user=uid).to_json()),
        'socials': json.loads(Social.objects(user=uid).to_json()),
        'portfolios': {
            'ojs': json.loads(OJ.objects(user=uid).to_json())
        },
        'skills': {
            'languages': json.loads(Language.objects(user=uid).to_json()),
            'frameworks': json.loads(Framework.objects(user=uid).to_json()),
            'platforms': json.loads(Platform.objects(user=uid).to_json()),
            'linguistics': json.loads(Linguistic.objects(user=uid).to_json())
        },
        'careers': {
            'academics': json.loads(Academic.objects(user=uid).to_json()),
            'achievements': json.loads(Achievement.objects(user=uid).to_json()),
            'certificates': json.loads(Certificate.objects(user=uid).to_json()),
            'experiences': json.loads(Experience.objects(user=uid).to_json())
        }
    }
    user.update(extra_sources)
    return user


@router.get("/id/{user_id}")
async def get_user(user_id: str):
    return json.loads(UserSchema(id=user_id).to_json())


@router.put("/")
def update_user(data: UserModel, token=Depends(JWTBearer())):
    uid = get_id_from_jwt(token)
    user = UserSchema.objects(id=uid)
    validate_authority(token, user.pk)
    user.update_one(
        name=data.name,
        fullName=data.fullName,
        avatar=data.avatar,
        coverimg=data.coverImg,
        yob=data.yob,
        address=data.address,
        degree=data.degree,
        phone=data.phone,
        title=data.title,
        whatIDo=data.whatIDo,
        about=data.about,
        usernmae=data.username,
        email=data.email,
        publicEmail=data.publicEmail,
    )

    return json.loads(user.to_json())



