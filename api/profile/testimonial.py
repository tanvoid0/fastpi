from typing import Optional

from pydantic import BaseModel


class TestimonialModel(BaseModel):
    title: str
    username: Optional[str]
    url: Optional[str]
    icon: Optional[str]
    image: Optional[str]
    progress: Optional[str]