from typing import Optional

from pydantic import BaseModel


class FactModel(BaseModel):
    quantity: str
    title: Optional[str]
    subtitle: Optional[str]