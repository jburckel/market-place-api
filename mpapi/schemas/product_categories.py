from typing import List
from pydantic import BaseModel

from ._commons import TreeObjectIdStr, MultiLanguageText, Image
from ._mixins import DBModel


class ProductCategoryTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None


class ProductCategoryBase(BaseModel):
    parentProductCategoryId: TreeObjectIdStr = None # None is root category
    name: str = None
    translations: ProductCategoryTranslations = None
    images: List[Image] = None


class ProductCategoryToInsert(BaseModel):
    name: str


class ProductCategoryToUpdate(BaseModel):
    pass


class ProductCategoryOut(DBModel, ProductCategoryBase):
    pass
