from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter

# origins = ["localhost", settings('DB_HOST'), "https://tan-pi.herokuapp.com", "herokuapp.com", "fastpi.tanv.me", "192.168.0.101:8000"]
from api.hobby import hobby
from api.linguistic import linguistic
from api.oj import oj
from api.organization import academic, achievement, certificate, experience
from api.password import password
from api.social import social
from api.todo import todo
from api import ping
from api.auth import auth
from api.skill import skill, platform, language, framework
from api.user import user
from settings.db import db_connect, db_disconnect

origins = ["*"]
app = FastAPI()


@app.on_event("startup")
async def startup():
    print("Server running")
    db_connect()
    pass


@app.on_event("shutdown")
async def shutdown():
    db_disconnect()
    print("Server shutting down")

# Cors Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(user.router)


# Skills
app.include_router(skill.router)
app.include_router(language.router)
app.include_router(framework.router)
app.include_router(platform.router)


# Organization
app.include_router(academic.router)
app.include_router(achievement.router)
app.include_router(certificate.router)
app.include_router(experience.router)

# Utilities
app.include_router(hobby.router)
app.include_router(oj.router)
app.include_router(social.router)
app.include_router(linguistic.router)
app.include_router(todo.router)

# Extra
app.include_router(password.router)
app.include_router(ping.router)


@app.get("/")
async def home():
    return "Welcome to the Blurry world of Pexels!"



# if __name__ == "__main__":
#     uvicorn.run("main:app --reload", host="localhost", port=8080, log_level="info", reload=True)
#     print("Application Running")
