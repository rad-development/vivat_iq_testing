from pydantic import BaseModel
from typing import Optional


class Config(BaseModel):
    base_url: Optional[str] = None
