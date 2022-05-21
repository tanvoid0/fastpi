from api.hobby.hobby import Hobby
from api.language.language import Language
from api.lib import *
from api.oj.oj import OJ
from api.organization.organization import Academic, Achievement, Certificate, Organization
from api.social.social import Social
from api.user.user import UserSchema

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


@router.get("/portfolio")
def get_portfolio(token=Depends(JWTBearer())):
    uid = get_id_from_jwt(token)
    user = UserSchema.objects(id=uid).get()
    academics = json.loads(Academic.objects(user=uid).to_json())
    achievements = json.loads(Achievement.objects(user=uid).to_json())
    certificates = json.loads(Certificate.objects(user=uid).to_json())
    experiences = json.loads(Organization.objects(user=uid).to_json())
    ojs = json.loads(OJ.objects(user=uid).to_json())

    ## TODO: Fix user reference (Stored as string rather than key for OJ user ReferenceField
    # user['skills']['oj'] = ojs
    #
    hobbies = json.loads(Hobby.objects(user=uid).to_json())
    languages = json.loads(Language.objects(user=uid).to_json())
    socials = json.loads(Social.objects(user=uid).to_json())
    user['hobbies'] = hobbies
    user['socials'] = socials
    user['languages'] = languages
    user['ojs'] = ojs
    user['academics'] = academics
    user['achievements'] = achievements
    user['certificates'] = certificates
    user['experiences'] = experiences
    user = json.loads(user.to_json())
    return user


@router.get("/{user_id}")
async def get_user(user_id: str):
    return json.loads(UserSchema(id=user_id).to_json())


