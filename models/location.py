from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'IR'