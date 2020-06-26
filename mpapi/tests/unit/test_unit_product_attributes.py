from bson import ObjectId

from mpapi.crud.product_attributes import ProductAttributes
from mpapi.schemas.product_attributes import ProductAttributeToInsert

valid_product_attribute = ProductAttributeToInsert.schema()["example"]
product_attribute_id = None

def test_create_product_attribute():
    global product_attribute_id, valid_product_attribute
    result = ProductAttributes.create_one(valid_product_attribute)
    assert result['success'] is True
    product_attribute_id = result['value']['_id']
    assert ObjectId(product_attribute_id)
    assert result['value']['name'] == valid_product_attribute["name"]


def test_update_product_attribute():
    global product_attribute_id
    name = "Test Update"
    result = ProductAttributes.update_one(product_attribute_id, {"name": name})
    assert result['success'] is True
    assert result['value']['name'] == name


def test_delete_product_attribute():
    global product_attribute_id
    result = ProductAttributes.delete_one(product_attribute_id)
    assert result['success'] is True
    result = ProductAttributes.get_one(product_attribute_id)
    assert result['success'] is False
