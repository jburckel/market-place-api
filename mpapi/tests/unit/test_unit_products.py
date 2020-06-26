from random import randrange
from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.products import Products
from mpapi.schemas.products import ProductToInsert

valid_product = ProductToInsert.schema()["example"]
product_id = None

def test_create_product():
    global product_id
    result = Products.create_one(valid_product)
    assert result['success'] is True
    product_id = result['value']['_id']
    assert ObjectId(product_id)
    assert result['value']['name'] == valid_product["name"]


def test_update_product():
    global product_id
    name = "Test Update"
    result = Products.update_one(product_id, {"name": name})
    print(result)
    assert result['success'] is True
    assert result['value']['name'] == name


def test_delete_product():
    global product_id
    result = Products.delete_one(product_id)
    assert result['success'] is True
    result = Products.get_one(product_id)
    assert result['success'] is False
