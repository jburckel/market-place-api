from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.products import Products
from mpapi.crud.users import get_current_user
from mpapi.schemas.users import UserOut
from mpapi.schemas.products import ProductToInsert, ProductToUpdate, ProductOut

router = APIRouter()

@router.get("/", response_model=List[ProductOut])
async def get_products(skip: int = 0, limit: int = 100):
    return Products.get_many(skip, limit)


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    return Products.get_one(product_id)


@router.post("/", response_model=ProductOut, status_code=201)
def create_product(product: ProductToInsert, current_user: UserOut = Depends(get_current_user)):
    product_id = Products.create_one(product)
    return Products.get_one(product_id)


@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    *,
    product_id: str = Path(..., title="The product ID as a valid ObjectId"),
    product: ProductToUpdate,
    current_user: UserOut = Depends(get_current_user)
):
    Products.update_one(product_id, product)
    return Products.get_one(product_id)


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: str, current_user: UserOut = Depends(get_current_user)):
    Products.delete_one(product_id)
