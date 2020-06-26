from bson import ObjectId

from pydantic import BaseModel, validator

from ._commons import ObjectIdStr, MultiLanguageText
from ._mixins import DBModel


class ProductAttributeValueTranslations(BaseModel):
    name: MultiLanguageText = None


class ProductAttributeValueBase(BaseModel):
    name: str = None
    translations: ProductAttributeValueTranslations = None
    productAttributeId: ObjectIdStr = None
    class Config:
        schema_extra = {
            'example': {
                'name': 'My Product Attribute Value',
                'translations': {
                    'name': {
                        'en': 'My product attribute value',
                        'fr': 'La valeur de mon attribut de produits',
                        'es': 'Mi producto atribuye valor'
                    },
                    'description': {
                        'en': 'My product attribute description',
                        'fr': 'La description de la valeur de mon attribut de produits',
                        'es': 'La descripción de mi producto atribuye valor'
                    }
                },
                'productAttributeId': str(ObjectId())
            }
        }


class ProductAttributeValueToInsert(ProductAttributeValueBase):
    name: str
    productAttributeId: ObjectIdStr


class ProductAttributeValueToUpdate(ProductAttributeValueBase):
    @validator('productAttributeId')
    def prevent_none(cls, v):
        assert v is not None, 'productAttributeId can not be set to None'
        return v


class ProductAttributeValueOut(DBModel, ProductAttributeValueBase):
    pass
