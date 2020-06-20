from random import randrange
from bson import ObjectId

from mpapi.crud.sellers import Sellers

valid_seller = {"name": f"Test {randrange(0, 10000)}"}

def test_create_seller():
    seller_id = Sellers.create_one(valid_seller)
    seller = Sellers.get_one(seller_id)
    assert seller["name"] == valid_seller["name"]
