from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(str(v)):
            return ValueError(f"Not a valid ObjectId: {v}")
        return str(v)

class ProductCreate(BaseModel):
    code: str
    description: str = None

class Product(ProductCreate):
    id: Optional[ObjectIdStr] = Field(..., alias="_id")
