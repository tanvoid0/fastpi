from api.model_lib import *


class TestimonialModel(BaseModel):
    title: str
    username: Optional[str]
    url: Optional[str]
    icon: Optional[str]
    image: Optional[str]
    progress: Optional[str]