from pydantic import BaseModel, Field
from typing import Optional
from .commons import CombinedOjectIdStr, MultiLanguageText


class ProductAttributeId(BaseModel):
    id: Optional[CombinedOjectIdStr] = Field(..., alias="_id")
    pass


class ProductAttributeTranslations(BaseModel):
    name: MultiLanguageText
    value: MultiLanguageText


class ProductAttribute(ProductAttributeId):
    translations: ProductAttributeTranslations = None
