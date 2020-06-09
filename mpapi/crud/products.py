from bson import ObjectId

from fastapi import HTTPException

from mpapi.core.database import get_collection
from mpapi.core.collection import COLLECTIONS
from .helpers import find_one_by_id, insert_one

products = get_collection(COLLECTIONS["PRODUCTS"])

def get_product_by_id(product_id: str) -> dict:
    return find_one_by_id(products, product_id)


def get_products(skip: int = 0, limit: int = 0, filters: dict = None) -> list:
    return [product for product in products.find(filters).skip(skip).limit(limit)]


def create_product(product: dict) -> str:
    return insert_one(products, product)
