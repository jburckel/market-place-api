from fastapi import HTTPException, Depends, status

from mpapi.core.auth import oauth2_scheme, decode_access_token
from mpapi.crud.users import Users
from mpapi.schemas.users import UserOut

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
    return UserOut(**user)
