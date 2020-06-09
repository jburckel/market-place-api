from pydantic import BaseModel, EmailStr
from typing import Optional

from .mixins import DBModel

class UserBase(BaseModel):
    username: str
    email: EmailStr
    firstname: str = None
    lastname: str = None

class UserIn(UserBase):
    password: str

class UserOut(DBModel, UserBase):
    email: Optional[EmailStr]

class UserInDB(UserBase):
    hashed_password: str

class UserOutDB(UserOut):
    hashed_password: str
