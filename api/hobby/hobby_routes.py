from api.lib import *
from api.hobby.hobby import Hobby, HobbyModel

router = APIRouter(
    prefix="/api/hobby",
    tags=["Hobby"]
)


@router.get("/")
def get_all_hobbies():
    return json.loads(Hobby.objects().to_json())


@router.get("/{hobby_id}")
def get_hobby(hobby_id: str):
    return json.loads(Hobby.objects(id=hobby_id).get().to_json())


@router.post("/")
def create_hobby(data: HobbyModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    hobby = Hobby(
        title=data.title,
        icon=data.icon,
        user=user
    ).save()
    return json.loads(hobby.to_json())


@router.put("/{hobby_id}")
def update_hobby(hobby_id: str, data: HobbyModel, token: str = Depends(JWTBearer)):
    hobby = Hobby.objects(id=hobby_id)
    validate_authority(token, hobby.get().user.pk)
    hobby.update_one(
        title=data.title,
        icon=data.icon
    )
    return json.loads(hobby.get().to_json())


@router.delete("/{hobby_id}")
def delete_hobby(hobby_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, hobby_id)
    return Hobby(id=hobby_id).delete()
