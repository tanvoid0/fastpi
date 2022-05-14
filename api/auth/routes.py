import json
import hashlib
from fastapi import HTTPException, status, APIRouter, Depends
from pydantic import SecretStr

from api.auth.utility import Authenticator, JWTBearer
from api.user import UserModel, User


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post('/register')
async def register(data: UserModel):
    if User.objects().get(email=data.email):
        print(json.loads(User(email=data.email).to_json()))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Already exists!")
    user = User(
        name=data.name,
        avatar=data.avatar,
        email=data.email,
        password=Authenticator.hash_text(data.password)
    ).save()
    print(user.to_json())
    response = json.loads(user.to_json())
    # response['token'] =
    return Authenticator.sign_jwt(user)


@router.post('/login')
async def login(email: str, password: str):
    print(password)
    user = User(
        email=email
    )
    print(user.to_json())
    print(user.password)
    print(Authenticator.hash_text(password))
    if len(user) <= 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")
    if user.password == Authenticator.hash_text(password):
        print("Matched")
        response = json.loads(user.to_json())
        response['token'] = Authenticator.sign_jwt(user)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")


@router.post('/validate', dependencies=[Depends(JWTBearer())])
async def validate():
    return "Validated"