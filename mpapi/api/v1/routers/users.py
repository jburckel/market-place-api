from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.users import Users
from mpapi.schemas.users import UserInInsert, UserInUpdate, UserOut

from ._exceptions import bad_request, not_found
from ._security import get_current_user

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def get_users(skip: int = 0, limit: int = 100):
    try:
        return Users.get_many(skip, limit)
    except:
        raise bad_request()


@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: str = Path(..., title="The user ID as a valid ObjectId")):
    try:
        user = Users.get_one(user_id)
        if not(user): raise
    except:
        raise not_found()


@router.post("/", response_model=UserOut, status_code=201)
def create_user(User: UserInInsert):
    try:
        user_id = Users.create_one(User)
        return Users.get_one(user_id)
    except Exception as e:
        raise bad_request(e)

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    *,
    user_id: str = Path(..., title="The user ID as a valid ObjectId"),
    User: UserInUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    try:
        Users.update_one(user_id, User)
        return Users.get_one(user_id)
    except Exception as e:
        raise bad_request(e)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: str):
    try:
        Users.delete_one(user_id)
    except Exception as e:
        raise bad_request()
