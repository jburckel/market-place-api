from bson import ObjectId

from typing import List
from pydantic import BaseModel, validator

from ._commons import ObjectIdStr, TreeObjectIdStr, MultiLanguageText, Image
from ._mixins import DBModel


class ProductCategoryTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None


class ProductCategoryBase(BaseModel):
    parentProductCategoryId: TreeObjectIdStr = None # None is root category
    name: str = None
    translations: ProductCategoryTranslations = None
    images: List[Image] = None
    sellerId: ObjectIdStr = None

    class Config:
        schema_extra = {
            'example': {
                'parentProductCategoryId': str(ObjectId()) + '/' + str(ObjectId()),
                'name': 'My product category',
                'translations': {
                    'name': {
                        'en': 'My product category',
                        'fr': 'Ma catégorie de produits',
                        'es': 'Mi categoría de productos'
                    },
                    'description': {
                        'en': 'My product category description',
                        'fr': 'Ma description de la catégorie de produits',
                        'es': 'La descripción de mi categoría de productos'
                    }
                },
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1560427450-00fa9481f01e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=639&q=80',
                        'description': {
                            'en': 'A wonderful category',
                            'fr': 'Une magnifique categorie',
                            'es': 'Una categoría magnífica'
                        }
                    }
                ],
                'sellerId': str(ObjectId())
            }
        }


class ProductCategoryToInsert(ProductCategoryBase):
    name: str
    sellerId: ObjectIdStr


class ProductCategoryToUpdate(ProductCategoryBase):
    @validator('sellerId')
    def prevent_none(cls, v):
        assert v is not None, 'sellerId can not be set to None'
        return v


class ProductCategoryOut(DBModel, ProductCategoryBase):
    pass
