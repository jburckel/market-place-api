from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.product_categories import ProductCategories
from mpapi.schemas.product_categories import ProductCategoryToInsert


url = '/api/v1/product-categories/'

valid_product_category = ProductCategoryToInsert.schema()["example"]
product_category_id = None


def test_get_product_categories(client):
    r = client.get(url)
    assert r.status_code == 200


def test_create_product_category_unauthorized(client):
    r = client.post(url, json=valid_product_category)
    assert r.status_code == 401


def test_create_product_category_bad_request_no_name(client, user_token):
    bad_product_category = valid_product_category.copy()
    del bad_product_category['name']
    r = client.post(url, headers=user_token, json=bad_product_category)
    assert r.status_code == 422


def test_create_product_category_authorized(client, user_token):
    global product_category_id
    r = client.post(url, headers=user_token, json=valid_product_category)
    assert r.status_code == 201
    product_category_id = r.json()["_id"]


def test_update_product_category_unauthorized(client):
    up_url = url + str(product_category_id)
    update_product_category = valid_product_category.copy()
    update_product_category["name"] = "Test-Update"
    del update_product_category["sellerId"]
    r = client.put(up_url, json=update_product_category)
    assert r.status_code == 401


def test_update_product_category_bad_request(client, user_token):
    up_url = url + str(product_category_id)
    update_product_category = valid_product_category.copy()
    update_product_category["name"] = "Test-Update"
    update_product_category["sellerId"] = None
    r = client.put(up_url, headers=user_token, json=update_product_category)
    assert r.status_code == 422


def test_update_product_category_authorized(client, user_token):
    up_url = url + str(product_category_id)
    update_product_category = valid_product_category.copy()
    update_product_category["name"] = "Test-Update"
    del update_product_category["sellerId"]
    r = client.put(up_url, headers=user_token, json=update_product_category)
    data = r.json()
    assert r.status_code == 200
    assert data["name"] == update_product_category["name"]


def test_delete_product_category_unauthorized(client):
    del_url = url + str(product_category_id)
    r = client.delete(del_url)
    assert r.status_code == 401


def test_delete_product_category_authorized(client, user_token):
    del_url = url + str(product_category_id)
    r = client.delete(del_url, headers=user_token)
    assert r.status_code == 204
    r = client.get(del_url)
    assert r.status_code == 404
