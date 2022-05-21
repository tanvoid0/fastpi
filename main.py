import os

from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app import router as api_router
ON_HEROKU = os.environ.get("ON_HEROKU")
if ON_HEROKU:
    port = int(os.environ.get("PORT", "17995"))
else:
    port = config('PORT')

app = FastAPI()
host = config('HOST')
host_url = str(host)+":"+str(port)
print(host_url)
origins = [host_url, config('DB_HOST'), "https://tan-pi.herokuapp.com", "herokuapp.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)

#
# if __name__ == "__main__":
#     uvicorn.run("main:app --reload", host=host, port=port, log_level="info", reload=True)
#     print("Application Running")
