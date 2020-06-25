from random import randrange
from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.sellers import Sellers
from mpapi.schemas.sellers import SellerToInsert

valid_seller = SellerToInsert.schema()["example"]

seller_id = None

def test_create_seller():
    global seller_id
    seller_id = Sellers.create_one(valid_seller)
    seller = Sellers.get_one(seller_id)
    assert seller["name"] == valid_seller["name"]


def test_update_seller():
    global seller_id
    valid_seller["name"] = "Test Update"
    Sellers.update_one(seller_id, valid_seller)
    seller = Sellers.get_one(seller_id)
    assert seller["name"] == valid_seller["name"]


def test_delete_seller():
    global seller_id
    Sellers.delete_one(seller_id)
    seller = None
    try:
        Sellers.get_one(seller_id)
    except Exception as e:
        assert str(e) == "Seller not found"
