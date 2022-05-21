from api.lib import *
from api.social.social import Social, SocialModel

router = APIRouter(
    prefix="/api/social",
    tags=["Social"]
)


@router.get("/")
def get_all_socials():
    return json.loads(Social.objects().to_json())


@router.get("/{social_id}")
def get_social(social_id: str, token: str = Depends(JWTBearer())):
    return json.loads(Social.objects(id=social_id).get().to_json())


@router.post("/")
def create_social(data: SocialModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    social = Social(
        name=data.name,
        url=data.url,
        icon=data.icon,
        user=user
    ).save()
    return json.loads(social.to_json())


@router.put("/{social_id}")
def update_social(social_id: str, data: SocialModel, token: str = Depends(JWTBearer())):
    social = validate_authority(social_id, Social, token)
    social.update(
        name=data.name,
        url=data.url,
        icon=data.icon
    )
    return json.loads(social.to_json())


@router.delete("/{social_id}")
def delete_social(social_id: str, token: str = Depends(JWTBearer())):
    validate_authority(social_id, Social, token)
    return Social(id=social_id)