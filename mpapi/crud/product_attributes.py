from mpapi.schemas.product_attributes import ProductAttributeToInsert, ProductAttributeToUpdate

from ._mixins import BaseCrud

class ProductAttributesCrud(BaseCrud):
    pass

ProductAttributes = ProductAttributesCrud("PRODUCT-ATTRIBUTES", ProductAttributeToInsert, ProductAttributeToUpdate)
