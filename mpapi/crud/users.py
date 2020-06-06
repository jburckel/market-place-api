from bson import ObjectId

from fastapi import HTTPException, Depends, status

from mpapi.core.auth import oauth2_scheme, decode_access_token
from mpapi.core.database import get_collection
from mpapi.crud.helpers import find_one_by_id, find_one_by_value


users = get_collection("users")


def get_user_by_id(user_id: str):
    return find_one_by_id(users, user_id)

def get_user_by_username(username: str):
    return find_one_by_value(users, 'username', username)

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
