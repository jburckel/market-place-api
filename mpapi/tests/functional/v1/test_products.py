from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.products import Products
from mpapi.schemas.products import ProductToInsert


url = '/api/v1/products/'

valid_product = ProductToInsert.schema()["example"]
product_id = None


def test_get_products(client):
    r = client.get(url)
    assert r.status_code == 200


def test_create_product_unauthorized(client):
    r = client.post(url, json=valid_product)
    assert r.status_code == 401


def test_create_product_bad_request_no_name(client, user_token):
    bad_product = valid_product.copy()
    del bad_product['name']
    r = client.post(url, headers=user_token, json=bad_product)
    assert r.status_code == 422


def test_create_product_authorized(client, user_token):
    global product_id
    r = client.post(url, headers=user_token, json=valid_product)
    assert r.status_code == 201
    product_id = r.json()["_id"]


def test_update_product_unauthorized(client):
    up_url = url + str(product_id)
    update_product = valid_product.copy()
    update_product["name"] = "Test-Update"
    del update_product["sellerId"]
    r = client.put(up_url, json=update_product)
    assert r.status_code == 401


def test_update_product_bad_request(client, user_token):
    up_url = url + str(product_id)
    update_product = valid_product.copy()
    update_product["name"] = "Test-Update"
    update_product["sellerId"] = None
    r = client.put(up_url, headers=user_token, json=update_product)
    assert r.status_code == 422


def test_update_product_authorized(client, user_token):
    up_url = url + str(product_id)
    update_product = valid_product.copy()
    update_product["name"] = "Test-Update"
    del update_product["sellerId"]
    r = client.put(up_url, headers=user_token, json=update_product)
    data = r.json()
    assert r.status_code == 200
    assert data["name"] == update_product["name"]


def test_delete_product_unauthorized(client):
    del_url = url + str(product_id)
    r = client.delete(del_url)
    assert r.status_code == 401


def test_delete_product_authorized(client, user_token):
    del_url = url + str(product_id)
    r = client.delete(del_url, headers=user_token)
    assert r.status_code == 204
    r = client.get(del_url)
    assert r.status_code == 404
