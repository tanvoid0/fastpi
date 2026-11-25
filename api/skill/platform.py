from api.lib import *
from api.skill.framework import get_framework
from api.skill.skill_model import Platform, PlatformModel

router = APIRouter(
    prefix="/api/platform",
    tags=["Platform"]
)


@router.get("/")
def get_all_platforms():
    platforms = Platform.objects().all()
    data = []
    for platform in platforms:
        data.append(get_platform(platform.pk))
    return data


@router.get("/{platform_id}")
def get_platform(platform_id: str):
    platform = Platform.objects(id=platform_id).get()
    frameworks = []
    for i in platform.frameworks:
        frameworks.append(get_framework(i))
    platform['frameworks'] = frameworks
    return json.loads(platform.to_json())


@router.post("/")
def create_platform(data: PlatformModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    platform = Platform(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description,
        frameworks=data.frameworks,
        user=user
    ).save()
    return json.loads(platform.to_json())


@router.put("/{platform_id}")
def update_platform(platform_id: str, data: PlatformModel, token: str = Depends(JWTBearer())):
    platform = Platform.objects(id=platform_id)
    validate_authority(token, platform.get().user.pk)
    platform.update_one(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description,
        frameworks=data.frameworks,
    )
    return json.loads(platform.get().to_json())


@router.delete("/{platform_id}")
def delete_platform(platform_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, platform_id)
    return Platform(id=platform_id).delete()

