from api.model_lib import *


class FactModel(BaseModel):
    quantity: str
    title: Optional[str]
    subtitle: Optional[str]