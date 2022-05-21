from api.lib import *
from api.skill.skill import Framework, FrameworkModel

router = APIRouter(
    prefix="/api/framework",
    tags=["Framework"]
)


@router.get("/")
def get_all_frameworks():
    return json.loads(Framework.objects().to_json())


@router.get("/{framework_id}")
def get_framework(framework_id: str):
    return json.loads(Framework.objects(id=framework_id).get().to_json())


@router.post("/")
def create_framework(data: FrameworkModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    framework = Framework(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description,
        language=data.language,
        user=user
    ).save()
    print("Working")
    return json.loads(framework.to_json())


@router.put("/{framework_id}")
def update_framework(framework_id: str, data: FrameworkModel, token: str = Depends(JWTBearer())):
    framework = Framework.objects(id=framework_id)
    validate_authority(token, framework.get().user.pk)
    framework.update_one(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description,
        language=data.language,
    )
    return json.loads(framework.get().to_json())


@router.delete("/{framework_id}")
def delete_framework(framework_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, framework_id)
    return Framework(id=framework_id).delete()

