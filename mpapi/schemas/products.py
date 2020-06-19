from pydantic import BaseModel
from typing import List

from .mixins import DBModel
from .commons import MultiLanguageText, Image, ObjectIdStr, CombinedOjectIdStr
from .product_attributes import ProductAttributeId
from .sellers import SellerOut


class ProductTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None
    short_description: MultiLanguageText = None


class ProductBase(BaseModel):
    productModelId: str = None #if None it's the productModel // is it better than a variant collection ???
    name: str = None
    translations: ProductTranslations = None
    sku: str = None
    mpn: str = None
    price: float = None
    priceCurrency: str = None
    images: List[Image] = None
    attributes: List[ProductAttributeId] = None
    secondaryAttributes: List[ProductAttributeId] = None
    sellerId: ObjectIdStr = None
    active: bool = None


class ProductToInsert(ProductBase):
    """
        When receiving a new product to insert, some fields are required and to
        define some default values
    """
    name: str
    active: bool = False
    sellerId: ObjectIdStr
    pass


class ProductToUpdate(ProductBase):
    """
        When receiving a product to update, it may be partial so every fields
        are optional. Used for validation and to remove unwanted values
    """
    pass


class ProductOut(DBModel, ProductBase):
    """
        When sending a product, we must include _id.
    """
    pass
