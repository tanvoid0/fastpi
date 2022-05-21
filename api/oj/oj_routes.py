from api.lib import *
from api.oj.oj import OJ, OJModel

router = APIRouter(
    prefix="/api/oj",
    tags=["OJ"]
)


@router.get("/")
def get_all_ojs():
    return json.loads(OJ.objects().to_json())


@router.get("/{oj_id}")
def get_oj(oj_id: str):
    return json.loads(OJ.objects(id=oj_id).get().to_json())


@router.post("/")
def create_oj(data: OJModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    oj = OJ(
        title=data.title,
        icon=data.icon,
        progress=data.progress,
        url=data.url,
        user=user
    ).save()
    return json.loads(oj.to_json())


@router.put("/{oj_id}")
def update_oj(oj_id: str, data: OJModel, token: str = Depends(JWTBearer)):
    oj = OJ.objects(id=oj_id)
    validate_authority(token, oj.get().user.pk)
    oj.update_one(
        title=data.title,
        icon=data.icon,
        progress=data.progress,
        url=data.url,
    )
    return json.loads(oj.get().to_json())


@router.delete("/{oj_id}")
def delete_oj(oj_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, oj_id)
    return OJ(id=oj_id).delete()
