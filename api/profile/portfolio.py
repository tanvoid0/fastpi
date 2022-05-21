from api.model_lib import *


class PortfolioModel(BaseModel):
    title: str
    username: Optional[str]
    url: Optional[str]
    icon: Optional[str]
    image: Optional[str]
    progress: Optional[str]