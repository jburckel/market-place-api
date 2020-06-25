from typing import List

from fastapi import APIRouter, Path, Depends

from mpapi.crud.products import Products
from mpapi.schemas.users import UserOut
from mpapi.schemas.products import ProductToInsert, ProductToUpdate, ProductOut

from ._exceptions import bad_request, not_found
from ._security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ProductOut])
async def get_products(skip: int = 0, limit: int = 100):
    try:
        return Products.get_many(skip, limit)
    except Exception:
        raise bad_request()


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    try:
        product = Products.get_one(product_id)
        if not(product): raise
        return product
    except Exception:
        raise not_found()


@router.post("/", response_model=ProductOut, status_code=201)
def create_product(Product: ProductToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
        raise bad_request("You can not create product before creating your seller account")
    else:
        Product.sellerId = CurrentUser.sellerId
    try:
        product_id = Products.create_one(Product)
        return Products.get_one(product_id)
    except Exception as e:
        raise bad_request(e)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    *,
    product_id: str = Path(..., title="The product ID as a valid ObjectId"),
    Product: ProductToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):

    try:
        # Exclude sellerId because it seems there is no reason to update it
        Products.update_one(product_id, Product, {'sellerId'})
        return Products.get_one(product_id)
    except Exception as e:
        raise bad_request(e)


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    try:
        Products.delete_one(product_id)
    except Exception as e:
        raise bad_request(e)
