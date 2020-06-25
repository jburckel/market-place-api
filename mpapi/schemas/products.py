from bson import ObjectId

from pydantic import BaseModel, validator
from typing import List

from .mixins import DBModel
from .commons import MultiLanguageText, Image, ObjectIdStr
from .product_attributes import ProductAttributeId
from .sellers import SellerOut


class ProductTranslations(BaseModel):
    title: MultiLanguageText = None
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
    attributeIds: List[ObjectIdStr] = None
    secondaryAttributeIds: List[ObjectIdStr] = None
    sellerId: ObjectIdStr = None
    active: bool = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'Test Product',
                'translations': {
                    'title': {
                        'en': 'A great product',
                        'fr': 'Un super produit',
                        'es': 'Un gran producto'
                    },
                    'description': {
                        'en': 'This awesome product is made up of several tricks, of undetermined size and color.',
                        'fr': 'Ce produit génial est composé de plusieurs trucs, de taille et de couleur indéterminé.',
                        'es': 'Este increíble producto está compuesto por varios trucos, de tamaño y color indeterminados.'
                    },
                    'short_description': {
                        'en': 'It is so good that you just have to buy it!',
                        'fr': "Il est tellement bien qu'il ne vous reste plus qu'à l'acheter !",
                        'es': '¡Es tan bueno que solo tienes que comprarlo!'
                    }
                },
                'sku': '12ab34cd',
                'mpn': '56ef78gh',
                'price': 12.6,
                'priceCurrency': 'EUR',
                'images': [
                    {
                        'url': 'https://images.unsplash.com/photo-1518953789413-9598f0909795?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
                        'description': {
                            'en': 'A wonderful product',
                            'fr': 'Un magnifique produit',
                            'es': 'Un producto maravilloso'
                        }
                    }
                ],
                'attributeIds': [
                    str(ObjectId()),
                    str(ObjectId())
                ],
                'secondaryAttributeIds': [
                    str(ObjectId()),
                    str(ObjectId())
                ],
                'sellerId': str(ObjectId()),
                'active': True
            }
        }


class ProductToInsert(ProductBase):
    """
        When receiving a new product to insert, some fields are required and to
        define some default values
    """
    name: str
    active: bool = False


class ProductToUpdate(ProductBase):
    """
        When receiving a product to update, it may be partial so every fields
        are optional. Used for validation and to remove unwanted values
    """
    @validator('sellerId')
    def prevent_none(cls, v):
        assert v is not None, 'sellerId may not be None'
        return v


class ProductOut(DBModel, ProductBase):
    """
        When sending a product, we must include _id.
    """
    pass
