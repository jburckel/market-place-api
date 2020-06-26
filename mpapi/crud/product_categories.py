from mpapi.schemas.product_categories import ProductCategoryToInsert, ProductCategoryToUpdate

from ._mixins import BaseCrud

class ProductCategoriesCrud(BaseCrud):
    pass

ProductCategories = ProductCategoriesCrud("PRODUCT-CATEGORIES", ProductCategoryToInsert, ProductCategoryToUpdate)
