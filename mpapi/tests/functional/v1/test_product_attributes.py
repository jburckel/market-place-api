from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.product_attributes import ProductAttributes
from mpapi.schemas.product_attributes import ProductAttributeToInsert


url = '/api/v1/product-attributes/'

valid_product_attribute = ProductAttributeToInsert.schema()["example"]
product_attribute_id = None


def test_get_product_attributes(client):
    r = client.get(url)
    assert r.status_code == 200


def test_create_product_attribute_unauthorized(client):
    r = client.post(url, json=valid_product_attribute)
    assert r.status_code == 401


def test_create_product_attribute_bad_request_no_name(client, user_token):
    bad_product_attribute = valid_product_attribute.copy()
    del bad_product_attribute['name']
    r = client.post(url, headers=user_token, json=bad_product_attribute)
    assert r.status_code == 422


def test_create_product_attribute_authorized(client, user_token):
    global product_attribute_id
    r = client.post(url, headers=user_token, json=valid_product_attribute)
    assert r.status_code == 201
    product_attribute_id = r.json()["_id"]


def test_update_product_attribute_unauthorized(client):
    up_url = url + str(product_attribute_id)
    update_product_attribute = valid_product_attribute.copy()
    update_product_attribute["name"] = "Test-Update"
    del update_product_attribute["sellerId"]
    r = client.put(up_url, json=update_product_attribute)
    assert r.status_code == 401


def test_update_product_attribute_bad_request(client, user_token):
    up_url = url + str(product_attribute_id)
    update_product_attribute = valid_product_attribute.copy()
    update_product_attribute["name"] = "Test-Update"
    update_product_attribute["sellerId"] = None
    r = client.put(up_url, headers=user_token, json=update_product_attribute)
    assert r.status_code == 422


def test_update_product_attribute_authorized(client, user_token):
    up_url = url + str(product_attribute_id)
    update_product_attribute = valid_product_attribute.copy()
    update_product_attribute["name"] = "Test-Update"
    del update_product_attribute["sellerId"]
    r = client.put(up_url, headers=user_token, json=update_product_attribute)
    data = r.json()
    assert r.status_code == 200
    assert data["name"] == update_product_attribute["name"]


def test_delete_product_attribute_unauthorized(client):
    del_url = url + str(product_attribute_id)
    r = client.delete(del_url)
    assert r.status_code == 401


def test_delete_product_attribute_authorized(client, user_token):
    del_url = url + str(product_attribute_id)
    r = client.delete(del_url, headers=user_token)
    assert r.status_code == 204
    r = client.get(del_url)
    assert r.status_code == 404
