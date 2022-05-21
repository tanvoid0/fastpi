import uvicorn
from decouple import config
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect

from api import password
from api.auth import auth_routes
from api.hobby import hobby_routes
from api.oj import oj_routes
from api.skill import skill_routes, language_routes, framework_routes, platform_routes
from api.social import social_routes
from api.todo import todo_routes
from api.language import tongue_routes
from api.user import user_routes

from api.organization import academic_routes, certificate_routes, achievement_routes, experience_routes


app = FastAPI()

# Initialize Database
connect(
    host=config("DB_HOST"),
)


router = APIRouter()

router.include_router(platform_routes.router)
router.include_router(framework_routes.router)
router.include_router(language_routes.router)

router.include_router(academic_routes.router)
router.include_router(achievement_routes.router)
router.include_router(certificate_routes.router)
router.include_router(experience_routes.router)

# Add all routers
router.include_router(auth_routes.router)
# router.include_router(employee.router)
router.include_router(hobby_routes.router)
router.include_router(oj_routes.router)
router.include_router(password.router)
router.include_router(skill_routes.router)
router.include_router(social_routes.router)
router.include_router(todo_routes.router)
router.include_router(tongue_routes.router)
router.include_router(user_routes.router)

@router.get("/")
async def home():
    return "Welcome to the Blurry world of Pexels!"


host = config('HOST')
port = config('PORT')
host_url = host+":"+port
origins = [host_url, config('DB_HOST')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#
if __name__ == "__main__":
    uvicorn.run("main:app --reload", host=host, port=port, log_level="info", reload=True)
    print("Application Running")