from api.lib import *
from api.skill.skill import Language, LanguageModel

router = APIRouter(
    prefix="/api/language",
    tags=["Language"]
)
#
#
# @router.get("/")
# def get_all_languages():
#     return json.loads(Language.objects().to_json())
#
#
# @router.get("/{language_id}")
# def get_language(language_id: str):
#     return json.loads(Language.objects(id=language_id).get().to_json())
#
#
# @router.post("/")
# def create_language(data: LanguageModel, token: str = Depends(JWTBearer())):
#     user = get_id_from_jwt(token)
#     language = Language(
#         title=data.title,
#         image=data.image,
#         fluency=data.fluency,
#         description=data.description,
#         user=user
#     ).save()
#     return json.loads(language.to_json())
#
#
# @router.put("/{language_id}")
# def update_language(language_id: str, data: LanguageModel, token: str = Depends(JWTBearer())):
#     language = Language.objects(id=language_id)
#     validate_authority(token, language.get().user.pk)
#     language.update_one(
#         title=data.title,
#         image=data.image,
#         fluency=data.fluency,
#         description=data.description
#     )
#     return json.loads(language.get().to_json())
#
#
# @router.delete("/{language_id}")
# def delete_language(language_id: str, token: str = Depends(JWTBearer())):
#     validate_authority(token, language_id)
#     return Language(id=language_id).delete()
#
