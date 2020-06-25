from bson import ObjectId

from fastapi.exceptions import HTTPException

from mpapi.crud.sellers import Sellers
from mpapi.schemas.sellers import SellerToInsert


url = '/api/v1/sellers/'

valid_seller = SellerToInsert.schema()["example"]
seller_id = None


def test_get_sellers(client):
    r = client.get(url)
    assert r.status_code == 200


def test_create_seller_unauthorized(client):
    r = client.post(url, json=valid_seller)
    assert r.status_code == 401


def test_create_seller_bad_request(client, user_token):
    bad_seller = valid_seller.copy()
    del bad_seller['name']
    r = client.post(url, headers=user_token, json=bad_seller)
    assert r.status_code == 422


def test_create_seller_authorized(client, user_token):
    global seller_id
    r = client.post(url, headers=user_token, json=valid_seller)
    assert r.status_code == 201
    seller_id = r.json()["_id"]
    r = client.get(url + str(seller_id))
    assert r.status_code == 200


def test_update_seller_unauthorized(client):
    up_url = url + str(seller_id)
    update_seller = valid_seller.copy()
    update_seller["name"] = "Test-Update"
    r = client.put(up_url, json=update_seller)
    assert r.status_code == 401


def test_update_seller_bad_request(client, user_token):
    up_url = url + str(seller_id)
    update_seller = valid_seller.copy()
    update_seller["name"] = None
    r = client.put(up_url, headers=user_token, json=update_seller)
    assert r.status_code == 422


def test_update_seller_authorized(client, user_token):
    up_url = url + str(seller_id)
    update_seller = valid_seller.copy()
    update_seller["name"] = "Test-Update"
    r = client.put(up_url, headers=user_token, json=update_seller)
    data = r.json()
    assert r.status_code == 200
    assert data["name"] == update_seller["name"]


def test_delete_seller_unauthorized(client):
    del_url = url + str(seller_id)
    r = client.delete(del_url)
    assert r.status_code == 401


def test_delete_seller_authorized(client, user_token):
    del_url = url + str(seller_id)
    r = client.delete(del_url, headers=user_token)
    assert r.status_code == 204
    r = client.get(del_url)
    print(r.json())
    assert r.status_code == 404
