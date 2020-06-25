from pydantic import BaseModel, Field
from typing import Optional
from .commons import ObjectIdStr, MultiLanguageText


class ProductAttributeId(BaseModel):
    id: Optional[ObjectIdStr] = Field(..., alias='_id')
    pass


class ProductAttributeTranslations(BaseModel):
    name: MultiLanguageText
    value: MultiLanguageText


class ProductAttribute(ProductAttributeId):
    translations: ProductAttributeTranslations = None
