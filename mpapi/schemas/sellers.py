from pydantic import BaseModel

from .mixins import DBModel
from .commons import Image, MultiLanguageText


class SellerTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None


class SellerBase(BaseModel):
    name: str = None
    translations: SellerTranslations = None
    logo: Image = None


class SellerToInsert(SellerBase):
    name: str


class SellerToUpdate(SellerBase):
    pass


class SellerOut(DBModel, SellerBase):
    pass
