from pydantic import BaseModel
from typing import List

from .mixins import DBModel
from .commons import MultiLanguageText, Image

class Variant(BaseModel):
    name: MultiLanguageText = None
    price: float = None

class ProductBase(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None
    sku: str = None
    mpn: str = None
    price: float = None
    priceCurrency: str = None
    short_description: MultiLanguageText = None
    image: List[Image] = None
    variant: List[Variant] = None


class ProductToInsert(ProductBase):
    """
        When receiving a new product to insert
        Some fields are required
    """
    code: str
    price: float
    pass


class ProductToUpdate(ProductBase):
    """
        When receiving a product to update
        It may be partial so every fields are optional
        Used for validation and to remove unwanted values
    """
    pass


class ProductOut(DBModel, ProductBase):
    """
        When sending a product, we must include _id
    """
    pass
