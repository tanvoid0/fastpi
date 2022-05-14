import json
import hashlib
from fastapi import HTTPException, status, APIRouter, Depends

from api.auth.utility import Authenticator, JWTBearer
from api.user import UserModel, User


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post('/register')
async def register(data: UserModel):
    if len(User(email=data.email)) > 0:
        print(json.loads(User(email=data.email).to_json()))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Already exists!")
    user = User(
        name=data.name,
        avatar=data.avatar,
        email=data.email,
        password=Authenticator.hash_text(data.password)
    ).save()
    print(user)
    return json.loads(user.to_json())


@router.post('/login')
async def login(data: UserModel):
    user = User(
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


@router.post('/validate', dependencies=[Depends(JWTBearer())])
async def validate():
    return "Validated"