from typing import List

from fastapi import APIRouter, Path, Depends

from mpapi.crud.products import Products
from mpapi.schemas.users import UserOut
from mpapi.schemas.products import ProductToInsert, ProductToUpdate, ProductOut

from ._exceptions import mpapi_exceptions
from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[ProductOut])
async def get_products(skip: int = 0, limit: int = 100):
    return format_result(Products.get_many(skip, limit))


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    return format_result(Products.get_one(product_id))


@router.post("/", response_model=ProductOut, status_code=201)
def create_product(Product: ProductToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
        raise mpapi_exceptions('PRODUCT-NO-SELLERID')
    Product.sellerId = CurrentUser.sellerId
    return format_result(Products.create_one(Product))


@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    *,
    product_id: str = Path(..., title="The product ID as a valid ObjectId"),
    Product: ProductToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    # Exclude sellerId because it seems there is no reason to update it
    return format_result(Products.update_one(product_id, Product, {'sellerId'}))


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(Products.delete_one(product_id))
