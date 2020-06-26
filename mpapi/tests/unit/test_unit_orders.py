from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.orders import Orders
from mpapi.schemas.orders import OrderToInsert


valid_order = OrderToInsert.schema()["example"]

order_id = None

def test_create_order():
    global order_id
    result = Orders.create_one(valid_order)
    assert result['success'] is True
    order_id = result['value']['_id']
    assert ObjectId(order_id)
    assert result["value"]["userId"] == valid_order["userId"]


def test_update_order():
    global order_id
    totalPrice = 999.999
    result = Orders.update_one(order_id, {'totalPrice': totalPrice})
    assert result['success'] is True
    assert result["value"]["totalPrice"] == totalPrice


def test_delete_order():
    global order_id
    result = Orders.delete_one(order_id)
    assert result["success"] is True
    result = Orders.get_one(order_id)
    assert result["success"] is False
