import uvicorn
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app import router as api_router

app = FastAPI()
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

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app --reload", host=host, port=port, log_level="info", reload=True)
    print("Application Running")
