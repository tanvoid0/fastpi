from api.lib import *
from api.skill.skill import Skill, SkillModel

router = APIRouter(
    prefix="/api/skill",
    tags=["Skill"]
)


@router.get("/")
def get_all_skills():
    return json.loads(Skill.objects().to_json())


@router.get("/{skill_id}")
def get_skill(skill_id: str):
    return json.loads(Skill.objects(id=skill_id).get().to_json())


@router.post("/")
def create_skill(data: SkillModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    skill = Skill(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description,
        user=user
    ).save()
    return json.loads(skill.to_json())


@router.put("/{skill_id}")
def update_skill(skill_id: str, data: SkillModel, token: str = Depends(JWTBearer())):
    skill = Skill.objects(id=skill_id)
    validate_authority(token, skill.get().user.pk)
    skill.update_one(
        title=data.title,
        image=data.image,
        fluency=data.fluency,
        description=data.description
    )
    return json.loads(skill.get().to_json())


@router.delete("/{skill_id}")
def delete_skill(skill_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, skill_id)
    return Skill(id=skill_id).delete()

