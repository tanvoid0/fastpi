import json
import hashlib
from fastapi import HTTPException, status, APIRouter, Depends, Request
from pydantic import SecretStr, BaseModel, Field

from api.auth.utility import JWTBearer, hash_text, sign_jwt, verify_hash, decode_jwt, get_id_from_jwt
from api.user import UserModel, User


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


class LoginModel(BaseModel):
    email: str = Field("new@mail.com", description="Enter email")
    password: str = Field("new123", description="Enter password")


@router.post('/register')
async def register(data: UserModel):
    if User.objects(email=data.email):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Already exists!")

    hashed_password = hash_text(data.password)
    user = User(
        name=data.name,
        avatar=data.avatar,
        email=data.email,
        password=hashed_password
    ).save()
    response = json.loads(user.to_json())
    response['token'] = sign_jwt(user)
    return response


@router.post('/login')
async def login(data: LoginModel):
    print(data.password)
    user = User.objects(email=data.email)
    if len(user) <= 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
    user = user.get()
    if verify_hash(text=data.password, hash_text=user.password):
        print("Matched")
        response = json.loads(user.to_json())
        response['token'] = sign_jwt(user)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")


@router.post('/authenticate')
async def validate(token: str = Depends(JWTBearer())) -> str | None:
    return get_id_from_jwt(token)
