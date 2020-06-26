from typing import Optional
from pydantic import BaseModel, Field

from ._commons import ObjectIdStr, MultiLanguageText
from ._mixins import DBModel

#
#
# Product Attribute
#
#


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
        assert v is not None, 'sellerId may not be None'
        return v


class ProductAttributeOut(DBModel, ProductAttributeBase):
    pass


#
#
# Product Attribute Value
#
#


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
        assert v is not None, 'productAttributeId may not be None'
        return v


class ProductAttributeValueOut(DBModel, ProductAttributeValueBase):
    pass
