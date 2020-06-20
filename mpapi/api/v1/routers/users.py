from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.users import Users
from mpapi.crud.users import get_current_user
from mpapi.schemas.users import UserIn, UserOut


router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def get_users(skip: int = 0, limit: int = 100):
    return Users.get_many(skip, limit)


@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: str = Path(..., title="The user ID as a valid ObjectId")):
    return Users.get_one(user_id)


@router.post("/", response_model=UserOut, status_code=201)
def create_user(user: UserIn):
    user_id = Users.create_one(user.dict())
    return Users.get_one(user_id)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: str):
    return Users.delete_one(user_id)
