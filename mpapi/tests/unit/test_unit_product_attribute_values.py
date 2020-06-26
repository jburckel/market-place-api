from bson import ObjectId

from mpapi.crud.product_attribute_values import ProductAttributeValues
from mpapi.schemas.product_attribute_values import ProductAttributeValueToInsert

valid_product_attribute_value = ProductAttributeValueToInsert.schema()["example"]
product_attribute_value_id = None

def test_create_product_attribute_value():
    global product_attribute_value_id, valid_product_attribute_value
    result = ProductAttributeValues.create_one(valid_product_attribute_value)
    assert result['success'] is True
    product_attribute_value_id = result['value']['_id']
    assert ObjectId(product_attribute_value_id)
    assert result['value']['name'] == valid_product_attribute_value["name"]


def test_update_product_attribute_value():
    global product_attribute_value_id
    name = "Test Update"
    result = ProductAttributeValues.update_one(product_attribute_value_id, {"name": name})
    assert result['success'] is True
    assert result['value']['name'] == name


def test_delete_product_attribute_value():
    global product_attribute_value_id
    result = ProductAttributeValues.delete_one(product_attribute_value_id)
    assert result['success'] is True
    result = ProductAttributeValues.get_one(product_attribute_value_id)
    assert result['success'] is False
