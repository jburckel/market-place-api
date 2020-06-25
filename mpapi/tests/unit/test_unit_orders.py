from random import randrange
from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.orders import Orders
from mpapi.schemas.orders import OrderToInsert


valid_order = OrderToInsert.schema()["example"]

order_id = None

def test_create_order():
    global order_id
    order_id = Orders.create_one(valid_order)
    order = Orders.get_one(order_id)
    assert order["userId"] == valid_order["userId"]


def test_update_order():
    global order_id
    totalPrice = 999.999
    Orders.update_one(order_id, {'totalPrice': totalPrice})
    order = Orders.get_one(order_id)
    assert order["totalPrice"] == totalPrice


def test_delete_order():
    global order_id
    Orders.delete_one(order_id)
    order = None
    try:
        Orders.get_one(order_id)
    except Exception as e:
        assert str(e) == "Order not found"
