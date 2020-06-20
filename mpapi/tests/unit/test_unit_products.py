from random import randrange
from bson import ObjectId

from mpapi.crud.products import Products

valid_product = {"name": f"Test {randrange(0, 10000)}", "sellerId": str(ObjectId())}

def test_create_product():
    product_id = Products.create_one(valid_product)
    product = Products.get_one(product_id)
    assert product["name"] == valid_product["name"]
