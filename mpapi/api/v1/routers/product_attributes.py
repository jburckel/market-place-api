from typing import List

from fastapi import APIRouter, Path, Depends

from mpapi.crud.product_attributes import ProductAttributes
from mpapi.schemas.users import UserOut
from mpapi.schemas.product_attributes import ProductAttributeToInsert, ProductAttributeToUpdate, ProductAttributeOut

from ._exceptions import mpapi_exceptions
from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[ProductAttributeOut])
async def get_product_attributes(skip: int = 0, limit: int = 100):
    return format_result(ProductAttributes.get_many(skip, limit))


@router.get("/{product_attribute_id}", response_model=ProductAttributeOut)
def get_product_attribute_by_id(product_attribute_id: str = Path(..., title="The product attribute ID as a valid ObjectId")):
    return format_result(ProductAttributes.get_one(product_attribute_id))


@router.post("/", response_model=ProductAttributeOut, status_code=201)
def create_product_attribute(ProductAttribute: ProductAttributeToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
        raise mpapi_exceptions({'error': 'USER-HAS-NO-SELLERID'})
    ProductAttribute.sellerId = CurrentUser.sellerId
    return format_result(ProductAttributes.create_one(ProductAttribute))


@router.put("/{product_attribute_id}", response_model=ProductAttributeOut)
def update_product_attribute(
    *,
    product_attribute_id: str = Path(..., title="The product_attribute ID as a valid ObjectId"),
    ProductAttribute: ProductAttributeToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    # Exclude sellerId because it seems there is no reason to update it
    return format_result(ProductAttributes.update_one(product_attribute_id, ProductAttribute, {'sellerId'}))


@router.delete("/{product_attribute_id}", status_code=204)
def delete_product_attribute(product_attribute_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(ProductAttributes.delete_one(product_attribute_id))
