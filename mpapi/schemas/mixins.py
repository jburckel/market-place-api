from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class ObjectIdStr(str):
    """
    id from MongoDB need to be valid ObjectId
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(str(v)):
            return ValueError(f"Not a valid ObjectId: {v}")
        return str(v)


class DBModel(BaseModel):
    id: Optional[ObjectIdStr] = Field(..., alias="_id")
