from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.sellers import Sellers
from mpapi.schemas.sellers import SellerToInsert

valid_seller = SellerToInsert.schema()["example"]

seller_id = None

def test_create_seller():
    global seller_id
    result = Sellers.create_one(valid_seller)
    assert result['success'] is True
    seller_id = result['value']['_id']
    assert ObjectId(seller_id)
    assert result['value']['name'] == valid_seller['name']


def test_update_seller():
    global seller_id
    valid_seller["name"] = "Test Update"
    result = Sellers.update_one(seller_id, valid_seller)
    assert result['success'] is True
    assert result['value']['name'] == valid_seller['name']


def test_delete_seller():
    global seller_id
    result = Sellers.delete_one(seller_id)
    assert result['success'] is True
    result = Sellers.get_one(seller_id)
    assert result['success'] is False
