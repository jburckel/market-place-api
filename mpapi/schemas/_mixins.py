from pydantic import BaseModel, Field
from typing import Optional
from ._commons import ObjectIdStr


class DBModel(BaseModel):
    id: Optional[ObjectIdStr] = Field(..., alias="_id")
