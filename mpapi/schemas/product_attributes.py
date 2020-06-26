from bson import ObjectId

from pydantic import BaseModel, validator

from ._commons import ObjectIdStr, MultiLanguageText
from ._mixins import DBModel


class ProductAttributeTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageText = None


class ProductAttributeBase(BaseModel):
    name: str = None
    translations: ProductAttributeTranslations = None
    sellerId: ObjectIdStr = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'My Product Attribute',
                'translations': {
                    'name': {
                        'en': 'My product attribute',
                        'fr': 'Mon attribut de produits',
                        'es': 'Mi producto atribuye'
                    },
                    'description': {
                        'en': 'My product attribute description',
                        'fr': 'La description de mon attribut de produits',
                        'es': 'La descripción de mi producto atribuye'
                    }
                },
                'sellerId': str(ObjectId())
            }
        }


class ProductAttributeToInsert(ProductAttributeBase):
    name: str
    sellerId: ObjectIdStr


class ProductAttributeToUpdate(ProductAttributeBase):
    @validator('sellerId')
    def prevent_none(cls, v):
        assert v is not None, 'sellerId can not be set to None'
        return v


class ProductAttributeOut(DBModel, ProductAttributeBase):
    pass
