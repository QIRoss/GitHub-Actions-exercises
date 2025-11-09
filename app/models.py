from pydantic import BaseModel
from typing import Optional

class HealthResponse(BaseModel):
    status: str
    version: str

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float