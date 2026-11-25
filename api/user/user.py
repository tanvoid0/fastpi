from api.lib import *
from api.hobby.hobby_model import Hobby
from api.linguistic.linguistic_model import Linguistic
from api.oj.oj_model import OJ
from api.organization.organization_model import Academic, Achievement, Certificate, Experience
from api.skill.framework import get_all_frameworks
from api.skill.language import get_all_languages
from api.skill.platform import get_all_platforms
from api.skill.skill_model import Language, Framework, Platform
from api.social.social_model import Social
from api.user.user_model import UserSchema, UserModel

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
    user = UserSchema.objects(username=username).exclude("password").get()
    uid = str(user.pk)
    user = json.loads(user.to_json())

    extra_sources = {
        'hobbies': json.loads(Hobby.objects(user=uid).to_json()),
        'socials': json.loads(Social.objects(user=uid).to_json()),
        'portfolios': {
            'ojs': json.loads(OJ.objects(user=uid).to_json())
        },
        'skills': {
            # 'languages': get_all_languages(),
            # 'frameworks': get_all_frameworks(),
            # 'platforms': get_all_platforms(),
            # 'linguistics': get_all_languages()
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



