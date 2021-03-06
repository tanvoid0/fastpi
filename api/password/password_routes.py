from api.lib import *
from api.password.password import Password, PasswordModel

router = APIRouter(
    prefix="/api/password",
    tags=['Password']
)


@router.get('/')
def get_all_passwords():
    aes = AESCipher()
    passwords = Password.objects()

    return json.loads(passwords.to_json())


@router.get('/{Id}')
def get_password(Id: str):
    data = Password.objects(id=Id).get()
    if data:
        aes = AESCipher()
        d = aes.decrypt(data.password)
        return d
    return json.loads(data.to_json())


@router.post('/')
def create_password(data: PasswordModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    aes = AESCipher()

    item = Password(
        website=data.website,
        name=data.name,
        username=data.username,
        password=aes.encrypt(data.password),
        category=data.category,
        note=data.note,
        type=data.type,
        user=user
    ).save()
    return json.loads(item.to_json())


@router.put('/{data_id}')
def update_password(data_id: str, data: PasswordModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    item = Password.objects(id=data_id).get()
    if user != str(item.user.pk):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not allowed to update the data")
    item.update(

    )
    return json.loads(item.to_json())


@router.delete("/{data_id}")
def delete_password(data_id: str):
    Password(id=data_id).delete()
    return
