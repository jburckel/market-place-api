from bson import ObjectId

from mpapi.crud.product_categories import ProductCategories
from mpapi.schemas.product_categories import ProductCategoryToInsert

valid_product_category = ProductCategoryToInsert.schema()["example"]
product_category_id = None

def test_create_product_category():
    global product_category_id, valid_product_category
    result = ProductCategories.create_one(valid_product_category)
    assert result['success'] is True
    product_category_id = result['value']['_id']
    assert ObjectId(product_category_id)
    assert result['value']['name'] == valid_product_category["name"]


def test_update_product_category():
    global product_category_id
    name = "Test Update"
    result = ProductCategories.update_one(product_category_id, {"name": name})
    assert result['success'] is True
    assert result['value']['name'] == name


def test_delete_product_category():
    global product_category_id
    result = ProductCategories.delete_one(product_category_id)
    assert result['success'] is True
    result = ProductCategories.get_one(product_category_id)
    assert result['success'] is False
