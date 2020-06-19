from pydantic import BaseModel, Field
from typing import Optional
from .commons import ObjectIdStr


class DBModel(BaseModel):
    id: Optional[ObjectIdStr] = Field(..., alias="_id")
