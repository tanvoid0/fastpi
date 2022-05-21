from api.model_lib import *


class LoginModel(BaseModel):
    email: str = Field("new@mail.com", description="Enter email")
    password: str = Field("new123", description="Enter password")