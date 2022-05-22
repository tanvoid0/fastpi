import os

import uvicorn
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app import router as api_router

origins = ["localhost", config('DB_HOST'), "https://tan-pi.herokuapp.com", "herokuapp.com", "fastpi.tanv.me"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app --reload", host="localhost", port=8080, log_level="info", reload=True)
    print("Application Running")
