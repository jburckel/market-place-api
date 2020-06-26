from pydantic import BaseModel, validator

from ._commons import ObjectIdStr, MultiLanguageText
from ._mixins import DBModel


class ProductAttributeTranslations(BaseModel):
    name: MultiLanguageText = None


class ProductAttributeBase(BaseModel):
    name: str = None
    translations: ProductAttributeTranslations = None
    sellerId: ObjectIdStr = None


class ProductAttributeToInsert(ProductAttributeBase):
    name: str
    sellerId: ObjectIdStr
    pass


class ProductAttributeToUpdate(ProductAttributeBase):
    @validator('sellerId')
    def prevent_none(cls, v):
        assert v is not None, 'sellerId can not be set to None'
        return v


class ProductAttributeOut(DBModel, ProductAttributeBase):
    pass
