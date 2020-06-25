from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.orders import Orders
from mpapi.schemas.orders import OrderToInsert


url = '/api/v1/orders/'

valid_order = OrderToInsert.schema()["example"]
order_id = None


def test_get_orders(client):
    r = client.get(url)
    assert r.status_code == 200


def test_create_order_unauthorized(client):
    r = client.post(url, json=valid_order)
    assert r.status_code == 401


def test_create_order_bad_request_no_total_price(client, user_token):
    bad_order = valid_order.copy()
    del bad_order['totalPrice']
    r = client.post(url, headers=user_token, json=bad_order)
    assert r.status_code == 422


def test_create_order_bad_request_wrong_seller_id(client, user_token):
    bad_order = valid_order.copy()
    bad_order['sellerId'] = "123456"
    r = client.post(url, headers=user_token, json=bad_order)
    assert r.status_code == 422


def test_create_order_authorized(client, user_token):
    global order_id
    r = client.post(url, headers=user_token, json=valid_order)
    print(r.json())
    assert r.status_code == 201
    order_id = r.json()["_id"]


def test_update_order_unauthorized(client):
    up_url = url + str(order_id)
    update_order = valid_order.copy()
    update_order["name"] = "Test-Update"
    del update_order["sellerId"]
    r = client.put(up_url, json=update_order)
    assert r.status_code == 401


def test_update_order_authorized(client, user_token):
    up_url = url + str(order_id)
    totalPrice = 999.99
    r = client.put(up_url, headers=user_token, json={'totalPrice': totalPrice})
    data = r.json()
    assert r.status_code == 200
    assert data["totalPrice"] == totalPrice


def test_delete_order_unauthorized(client):
    del_url = url + str(order_id)
    r = client.delete(del_url)
    assert r.status_code == 401


def test_delete_order_authorized(client, user_token):
    del_url = url + str(order_id)
    r = client.delete(del_url, headers=user_token)
    assert r.status_code == 204
    r = client.get(del_url)
    assert r.status_code == 404
