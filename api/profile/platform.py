from api.model_lib import *

class PlatformModel(BaseModel):
    name: str
    stacks: Optional[list]


class Platform(DynamicDocument):
    name = StringField()
    stacks = ListField()


