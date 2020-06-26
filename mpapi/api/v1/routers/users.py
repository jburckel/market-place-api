from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.users import Users
from mpapi.schemas.users import UserInInsert, UserInUpdate, UserOut

from ._security import get_current_user
from ._utils import format_result

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def get_users(skip: int = 0, limit: int = 100):
    return format_result(Users.get_many(skip, limit))


@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: str = Path(..., title="The user ID as a valid ObjectId")):
    return format_result(Users.get_one(user_id))


@router.post("/", response_model=UserOut, status_code=201)
def create_user(User: UserInInsert):
    return format_result(Users.create_one(User))

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    *,
    user_id: str = Path(..., title="The user ID as a valid ObjectId"),
    User: UserInUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    return format_result(Users.update_one(user_id, User))

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: str):
    return format_result(Users.delete_one(user_id))
