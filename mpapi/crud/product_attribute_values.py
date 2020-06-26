from mpapi.schemas.product_attribute_values import ProductAttributeValueToInsert, ProductAttributeValueToUpdate

from ._mixins import BaseCrud

class ProductAttributeValuesCrud(BaseCrud):
    pass

ProductAttributeValues = ProductAttributeValuesCrud("PRODUCT-ATTRIBUTE-VALUES", ProductAttributeValueToInsert, ProductAttributeValueToUpdate)
