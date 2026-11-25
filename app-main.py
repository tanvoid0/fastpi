# from decouple import settings
# from fastapi import APIRouter
# from mongoengine import connect
#
# # from api import password
# from app.api.auth import auth
# from app.api.hobby import hobby_routes
# from app.api.oj import oj_routes
# from app.api.skill import skill_routes, platform_routes, framework_routes, language_routes
# from app.api.social import social_routes
# from app.api.todo import todo_routes
# from app.api.linguistic import linguistic_routes
# from app.api.user import user_routes
#
# from app.api.organization import academic_routes, achievement_routes
# from app.api.organization import certificate_routes, experience_routes
#
# # Initialize Router
#
# router = APIRouter()
#
# # Initialize Database
# connect(
#     # db=settings("DB"),
#     host=settings("DB_HOST"),
#     # username=settings("USERNAME"),
#     # password=settings("PASSWORD")
# )
#
# router.include_router(platform_routes.router)
# router.include_router(framework_routes.router)
# router.include_router(language_routes.router)
#
# router.include_router(academic_routes.router)
# router.include_router(achievement_routes.router)
# router.include_router(certificate_routes.router)
# router.include_router(experience_routes.router)
#
# # Add all routers
# router.include_router(auth_routes.router)
# # router.include_router(employee.router)
# router.include_router(hobby_routes.router)
# router.include_router(oj_routes.router)
# # router.include_router(password.router)
# router.include_router(skill_routes.router)
# router.include_router(social_routes.router)
# router.include_router(todo_routes.router)
# router.include_router(linguistic_routes.router)
# router.include_router(user_routes.router)
#
#
#
