from mpapi.schemas.products import ProductToInsert, ProductToUpdate

from ._mixins import BaseCrud

class ProductsCrud(BaseCrud):
    pass

Products = ProductsCrud("PRODUCTS", ProductToInsert, ProductToUpdate)
