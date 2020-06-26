from pydantic import BaseModel, validator

from ._commons import ObjectIdStr, MultiLanguageText
from ._mixins import DBModel


class ProductAttributeValueTranslations(BaseModel):
    name: MultiLanguageText = None


class ProductAttributeValueBase(BaseModel):
    name: str = None
    translations: ProductAttributeValueTranslations = None
    productAttributeId: ObjectIdStr = None


class ProductAttributeValueToInsert(BaseModel):
    name: str
    productAttributeId: ObjectIdStr
    pass


class ProductAttributeValueToUpdate(BaseModel):
    @validator('productAttributeId')
    def prevent_none(cls, v):
        assert v is not None, 'productAttributeId can not be set to None'
        return v


class ProductAttributeValueOut(DBModel, ProductAttributeValueBase):
    pass
