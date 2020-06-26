from mpapi.core.auth import get_password_hash
from mpapi.schemas.users import UserToInsert, UserToUpdate, UserInInsert, UserInUpdate, UserOut

from ._mixins import BaseCrud

class UsersCrud(BaseCrud):

    def create_one(self, User):
        User = self.validate_fields(User, UserInInsert)
        hashed_password = get_password_hash(User.password)
        User = UserToInsert(**User.dict(), hashed_password=hashed_password)
        return super().create_one(User)


    def update_one(self, user_id: str, User):
        if hasattr(User, 'password'):
            User = self.validate_fields(User, UserInUpdate)
            hashed_password = get_password_hash(User.password)
            User = UserToUpdate(**User.dict(), hashed_password=hashed_password)
        return super().update_one(user_id, User)


Users = UsersCrud("USERS", UserToInsert, UserToUpdate)
