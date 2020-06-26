from pydantic import BaseModel, EmailStr
from typing import Optional

from ._commons import ObjectIdStr
from ._mixins import DBModel


class UserBase(BaseModel):
    username: str = None
    email: EmailStr = None
    firstname: str = None
    lastname: str = None
    sellerId: ObjectIdStr = None


class UserInInsert(UserBase):
    username: str
    email: EmailStr
    password: str


class UserToInsert(UserBase):
    username: str
    email: EmailStr
    hashed_password: str


class UserInUpdate(UserBase):
    password: str = None


class UserToUpdate(UserBase):
    pass


class UserOut(DBModel, UserBase):
    pass
