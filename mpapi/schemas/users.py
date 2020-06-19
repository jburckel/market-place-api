from pydantic import BaseModel, EmailStr
from typing import Optional

from .mixins import DBModel
from .commons import ObjectIdStr

class UserBase(BaseModel):
    username: str = None
    email: EmailStr = None
    hashed_password: str = None
    firstname: str = None
    lastname: str = None
    sellerId: ObjectIdStr = None


class UserIn(UserBase):
    username: str
    email: EmailStr
    password: str


class UserToInsert(UserBase):
    username: str
    email: EmailStr
    hashed_password: str


class UserToUpdate(UserBase):
    pass


class UserOut(DBModel, UserBase):
    pass
