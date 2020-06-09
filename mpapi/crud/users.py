from bson import ObjectId

from fastapi import HTTPException, Depends, status

from mpapi.core.auth import oauth2_scheme, decode_access_token, get_password_hash
from mpapi.core.database import get_collection
from mpapi.crud.helpers import find_one_by_id, find_one_by_value, insert_one
from mpapi.schemas.users import UserIn, UserInDB


users = get_collection("users")

def get_user_by_id(user_id: str) -> dict:
    return find_one_by_id(users, user_id)


def get_user_by_username(username: str) -> dict:
    return find_one_by_value(users, 'username', username)


def get_users(skip: int = 0, limit: int = 0, filters: dict = None) -> list:
    return [user for user in users.find(filters).skip(skip).limit(limit)]


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    id = decode_access_token(token)
    if id is None:
        raise credentials_exception
    user = get_user_by_id(id)
    if user is None:
        raise credentials_exception
    return user


def create_user(user: UserIn) -> str:
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    return insert_one(users, user_in_db.dict())
