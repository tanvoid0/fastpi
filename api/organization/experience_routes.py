from api.lib import *
from api.organization.organization import Experience, ExperienceModel


router = APIRouter(
    prefix="/api/experience",
    tags=["Experience"]
)


@router.get("/")
def get_all_experiences():
    return json.loads(Experience.objects().to_json())


@router.get("/{experience_id}")
def get_experience(experience_id: str):
    return json.loads(Experience.objects(id=experience_id).get().to_json())


@router.post("/")
def create_experience(data: ExperienceModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    experience = Experience(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        role=data.role,
        user=user
    ).save()
    return json.loads(experience.to_json())


@router.put("/{experience_id}")
def update_experience(experience_id: str, data: ExperienceModel, token: str = Depends(JWTBearer)):
    experience = Experience.objects(id=experience_id)
    validate_authority(token, experience.get().user.pk)
    experience.update_one(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        role=data.role,
    )
    return json.loads(experience.get().to_json())


@router.delete("/{experience_id}")
def delete_experience(experience_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, experience_id)
    return Experience(id=experience_id).delete()
