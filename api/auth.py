import os
import time
from typing import Dict
import hashlib

import jwt
from decouple import config
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.user import UserModel, UserSchema
from app import app, json, HTTPException, status

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.schema == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")


    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = Authenticator.decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid


class Authenticator:
    salt = os.urandom(32)

    @staticmethod
    def sign_jwt(user_id: str) -> Dict[str, str]:
        payload = {
            'user_id': user_id,
            'expires': time.time() + 600
        }
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


    @staticmethod
    def decode_jwt(token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token['expires'] >= time.time() else None
        except:
            return {}

    @staticmethod
    def hash_text(__self__, plain_text: str):
        digest = hashlib.pbkdf2_hmac('sha256', plain_text.encode(), salt=__self__.salt, iterations=1000)
        return digest.hex()



@app.post('/auth/register', tags=['Auth'])
async def register(data: UserModel):
    if len(UserSchema(email=data.email)) > 0 :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Already exists!")
    user = UserSchema(
        name=data.name,
        avatar=data.avatar,
        email=data.email,
        password=Authenticator.hash_text(data.password)
    ).save()
    return json.loads(user.to_json())


@app.post('/auth/login', tags=['Auth'])
async def login(data: UserModel):
    user = UserSchema(
        email=data.email,
        password=hashlib.sha256(data.password).hexdigest()
    )
    if len(user) <= 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
    if user.password == Authenticator.hash_text(data.password) :
        response = json.loads(user.to_json())
        response['token'] = Authenticator.sign_jwt(data.email)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

