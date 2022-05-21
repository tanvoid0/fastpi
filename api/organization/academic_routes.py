from api.lib import *
from api.organization.organization import Academic, AcademicModel


router = APIRouter(
    prefix="/api/academic",
    tags=["Academic"]
)


@router.get("/")
def get_all_academics():
    return json.loads(Academic.objects().to_json())


@router.get("/{academic_id}")
def get_academic(academic_id: str):
    return json.loads(Academic.objects(id=academic_id).get().to_json())


@router.post("/")
def create_academic(data: AcademicModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    academic = Academic(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        graduation=data.graduation,
        user=user
    ).save()
    return json.loads(academic.to_json())


@router.put("/{academic_id}")
def update_academic(academic_id: str, data: AcademicModel, token: str = Depends(JWTBearer)):
    academic = Academic.objects(id=academic_id)
    validate_authority(token, academic.get().user.pk)
    academic.update_one(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        graduation=data.graduation,
    )
    return json.loads(academic.get().to_json())


@router.delete("/{academic_id}")
def delete_academic(academic_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, academic_id)
    return Academic(id=academic_id).delete()
