from bson import ObjectId

from fastapi import HTTPException, Depends, status

from mpapi.core.auth import oauth2_scheme, decode_access_token, get_password_hash
from mpapi.schemas.users import UserToInsert, UserToUpdate, UserIn

from .mixins import BaseCrud

class UsersCrud(BaseCrud):
    def create_one(self, user: dict):
        user['hashed_password'] = get_password_hash(user["password"])
        del user['password']
        return super().create_one(user)

Users = UsersCrud("USERS", UserToInsert, UserToUpdate)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    id = decode_access_token(token)
    if id is None:
        raise credentials_exception
    user = Users.get_one(id)
    if user is None:
        raise credentials_exception
    return user
