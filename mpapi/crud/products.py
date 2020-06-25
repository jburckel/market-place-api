from bson import ObjectId

from mpapi.schemas.products import ProductToInsert, ProductToUpdate

from ._mixins import BaseCrud

class ProductBase(BaseCrud):
    pass

Products = ProductBase("PRODUCTS", ProductToInsert, ProductToUpdate)
