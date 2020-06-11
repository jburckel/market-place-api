from bson import ObjectId

from fastapi import HTTPException

from mpapi.core.database import get_collection
from mpapi.core.collection import COLLECTIONS
from mpapi.schemas.products import ProductToInsert, ProductToUpdate
from .helpers import find_one_by_id, insert_one, update_one_by_id

products = get_collection(COLLECTIONS["PRODUCTS"])


def get_product_by_id(product_id: str) -> dict:
    return find_one_by_id(products, product_id)


def get_products(skip: int = 0, limit: int = 0, filters: dict = None) -> list:
    """
        First validate filters
        Then get all products matching filters with the limit indicated
        Finally return the list of products
    """
    return [product for product in products.find(filters).skip(skip).limit(limit)]


def create_product(product: ProductToInsert) -> str:
    """
        First insert product in DB
        Finally return the DB id of new product
    """
    return insert_one(products, product.dict())


def update_product(product_id: str, product: ProductToUpdate):
    """
        From pydantic Model, keep only explicitly set fields
        Then validate some values
        Finally update DB

    """
    values_to_update = product.dict(exclude_unset=True)
    no_none_fields = ['code']
    for field in no_none_fields:
        if field in values_to_update and values_to_update[field] is None:
            del values_to_update[field]
    update_one_by_id(products, product_id, values_to_update)
