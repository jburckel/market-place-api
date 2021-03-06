from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


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
            raise ValueError(f"Not a valid ObjectId: {v}")
        return str(v)


class CombinedObjectIdStr(str):
    """
    Combined Id this a combinaison of two ObjectIds seperate by =
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        objid1, objid2 = v.split("=")
        if not ObjectId.is_valid(str(objid1)) or not ObjectId.is_valid(str(objid2)):
            raise ValueError(f"Not a valid ObjectId: {v}")
        return str(v)


class TreeObjectIdStr(str):
    """
    Combined Id this a combinaison of several ObjectIds seperate by /
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        listObj = v.split("/")
        for obj in listObj:
            if not ObjectId.is_valid(str(obj)):
                raise ValueError(f"Not a valid ObjectId: {v}")
        return str(v)


class MultiLanguageText(BaseModel):
    en: str = None
    es: str = None
    fr: str = None


class Address(BaseModel):
    name: str = None
    addressLine1: str
    addressLine2: str = None
    postalCode: str = None
    town: str = None
    state: str = None
    country: str


class Image(BaseModel):
    url: str
    description: MultiLanguageText = None
