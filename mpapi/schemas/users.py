from pydantic import BaseModel
from typing import Optional

from .mixins import DBModel


class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class User(DBModel, UserCreate):
    hashed_password: str
