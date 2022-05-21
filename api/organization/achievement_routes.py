from api.lib import *
from api.organization.organization import Achievement, AchievementModel


router = APIRouter(
    prefix="/api/achievement",
    tags=["Achievement"]
)


@router.get("/")
def get_all_achievements():
    return json.loads(Achievement.objects().to_json())


@router.get("/{achievement_id}")
def get_achievement(achievement_id: str):
    return json.loads(Achievement.objects(id=achievement_id).get().to_json())


@router.post("/")
def create_achievement(data: AchievementModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    achievement = Achievement(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        achievement=data.achievement,
        user=user
    ).save()
    return json.loads(achievement.to_json())


@router.put("/{achievement_id}")
def update_achievement(achievement_id: str, data: AchievementModel, token: str = Depends(JWTBearer)):
    achievement = Achievement.objects(id=achievement_id)
    validate_authority(token, achievement.get().user.pk)
    achievement.update_one(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        achievement=data.achievement,
    )
    return json.loads(achievement.get().to_json())


@router.delete("/{achievement_id}")
def delete_achievement(achievement_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, achievement_id)
    return Achievement(id=achievement_id).delete()
