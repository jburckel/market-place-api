from typing import List

from fastapi import APIRouter, Path, Depends

from mpapi.crud.product_attribute_values import ProductAttributeValues
from mpapi.schemas.users import UserOut
from mpapi.schemas.product_attribute_values import ProductAttributeValueToInsert, ProductAttributeValueToUpdate, ProductAttributeValueOut

from ._exceptions import mpapi_exceptions
from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[ProductAttributeValueOut])
async def get_product_attribute_values(skip: int = 0, limit: int = 100):
    return format_result(ProductAttributeValues.get_many(skip, limit))


@router.get("/{product_attribute_value_id}", response_model=ProductAttributeValueOut)
def get_product_attribute_value_by_id(product_attribute_value_id: str = Path(..., title="The product attribute ID as a valid ObjectId")):
    return format_result(ProductAttributeValues.get_one(product_attribute_value_id))


@router.post("/", response_model=ProductAttributeValueOut, status_code=201)
def create_product_attribute_value(ProductAttributeValue: ProductAttributeValueToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(ProductAttributeValues.create_one(ProductAttributeValue))


@router.put("/{product_attribute_value_id}", response_model=ProductAttributeValueOut)
def update_product_attribute_value(
    *,
    product_attribute_value_id: str = Path(..., title="The product_attribute_value ID as a valid ObjectId"),
    ProductAttributeValue: ProductAttributeValueToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    # Exclude sellerId because it seems there is no reason to update it
    return format_result(ProductAttributeValues.update_one(product_attribute_value_id, ProductAttributeValue, {'sellerId'}))


@router.delete("/{product_attribute_value_id}", status_code=204)
def delete_product_attribute_value(product_attribute_value_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(ProductAttributeValues.delete_one(product_attribute_value_id))
