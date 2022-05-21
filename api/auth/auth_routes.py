# import json
#
# from fastapi import HTTPException, status, APIRouter, Depends
# from pydantic import BaseModel, Field
#
# from service.enigma.enigma_aes import AESCipher
# from service.jwt_bearer import JWTBearer, PasswordHasher, sign_jwt, get_id_from_jwt
# from api.user.user import UserModel, UserSchema
from api.auth.auth_model import LoginModel
from api.lib import *
from api.user.user import UserModel, UserSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post('/register')
async def register(data: UserModel):
    if UserSchema.objects(email=data.email):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Already exists!")

    hashed_password = PasswordHasher.hash_text(data.password)
    user = UserSchema(
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
    user = UserSchema.objects(email=data.email)
    if len(user) <= 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
    user = user.get()
    if PasswordHasher.verify_hash(text=data.password, hash_text=user.password):
        print("Matched")
        response = json.loads(user.to_json())
        response['token'] = sign_jwt(user)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")


@router.post('/authenticate')
async def validate(token: str = Depends(JWTBearer())) -> str | None:
    return get_id_from_jwt(token)


@router.post('/token')
async def token(data: LoginModel):
    user = UserSchema.objects(email=data.email)
    if len(user) <= 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
    user = user.get()
    if PasswordHasher.verify_hash(text=data.password, hash_text=user.password):
        return JSONResponse(sign_jwt(user))
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

@router.post("/enc")
def encrypt(data: str):
    aes = AESCipher()
    return aes.encrypt(data)


@router.post("/dec")
def decrypt(data: str):
    aes = AESCipher()
    return aes.decrypt(data)
