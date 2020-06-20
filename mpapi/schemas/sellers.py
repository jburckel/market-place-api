from pydantic import BaseModel, validator

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
    @validator('name')
    def prevent_none(cls, v):
        assert v is not None and v != '', 'Name may not be None or empty string'
        return v


class SellerOut(DBModel, SellerBase):
    pass
