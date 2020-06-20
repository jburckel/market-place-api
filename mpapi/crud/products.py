from bson import ObjectId

from .mixins import BaseCrud
from mpapi.schemas.products import ProductToInsert, ProductToUpdate

class ProductBase(BaseCrud):
    pass

Products = ProductBase("PRODUCTS", ProductToInsert, ProductToUpdate)
