from api.lib import *
from api.linguistic.linguistic import Linguistic, LinguisticModel

router = APIRouter(
    prefix="/api/linguistic",
    tags=["Linguistic"]
)


@router.get("/")
def get_all_linguistics():
    return json.loads(Linguistic.objects().to_json())


@router.get("/{linguistic_id}")
def get_linguistic(linguistic_id: str):
    return json.loads(Linguistic.objects(id=linguistic_id).get().to_json())


@router.post("/")
def create_linguistic(data: LinguisticModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    linguistic = Linguistic(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        user=user
    ).save()
    return json.loads(linguistic.to_json())


@router.put("/{linguistic_id}")
def update_linguistic(linguistic_id: str, data: LinguisticModel, token: str = Depends(JWTBearer)):
    linguistic = Linguistic.objects(id=linguistic_id)
    validate_authority(token, linguistic.get().user.pk)
    linguistic.update_one(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
    )
    return json.loads(linguistic.get().to_json())


@router.delete("/{linguistic_id}")
def delete_linguistic(linguistic_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, linguistic_id)
    return Linguistic(id=linguistic_id).delete()
