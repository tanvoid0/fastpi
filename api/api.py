import json
from typing import Optional

import uvicorn
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from mongoengine import connect

app = FastAPI()

@app.get("/")
async def home():
    return "Welcome to FASTPI"
