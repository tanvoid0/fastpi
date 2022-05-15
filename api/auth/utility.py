import os
from datetime import datetime
from typing import Any

import jwt
import time
from passlib.context import CryptContext

from decouple import config
from fastapi import Request, HTTPException, status, APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.user import UserModel, User

JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")
salt = os.urandom(32)
passContext = CryptContext(schemes=['bcrypt'], deprecated='auto')


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid


def sign_jwt(user: User) -> dict:
    payload = {
        'id': str(user.pk),
        'email': user.email,
        'expires': time.time() + 3600
    }
    print(payload)
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}


def get_id_from_jwt(token: str) -> str | None:
    res = decode_jwt(token)
    if res == {}:
        return None
    return res['id']


def hash_text(plain_text):
    return passContext.hash(plain_text)


def verify_hash(text: str, hash_text: str):
    return passContext.verify(text, hash_text)

