from random import randrange
from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.products import Products
from mpapi.schemas.products import ProductToInsert

valid_product = ProductToInsert.schema()["example"]
product_id = None

def test_create_product():
    global product_id
    product_id = Products.create_one(valid_product)
    product = Products.get_one(product_id)
    assert product["name"] == valid_product["name"]


def test_update_product():
    global product_id
    name = "Test Update"
    Products.update_one(product_id, {"name": name})
    product = Products.get_one(product_id)
    assert product["name"] == name


def test_delete_product():
    global product_id
    Products.delete_one(product_id)
    product = None
    try:
        Products.get_one(product_id)
    except Exception as e:
        assert str(e) == "Product not found"
