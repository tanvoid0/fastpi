from decouple import config
from fastapi import APIRouter
from mongoengine import connect

from api import employee, user, todo, password
from api.auth import routes

# Initialize Router

router = APIRouter()

# Initialize Database
connect(
    # db=config("DB"),
    host=config("DB_HOST"),
    # username=config("USERNAME"),
    # password=config("PASSWORD")
)

# Add all routers
router.include_router(routes.router)
router.include_router(employee.router)
router.include_router(user.router)
router.include_router(todo.router)
router.include_router(password.router)


@router.get("/")
async def home():
    return
