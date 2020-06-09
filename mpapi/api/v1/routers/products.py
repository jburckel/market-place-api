from fastapi import APIRouter, Path, Depends
from typing import List

import mpapi.crud.products as crud
from mpapi.crud.users import get_current_user
from mpapi.schemas.users import UserOut
from mpapi.schemas.products import ProductIn, ProductOut

router = APIRouter()

@router.get("/", response_model=List[ProductOut])
async def get_products(skip: int = 0, limit: int = 100):
    return crud.get_products(skip, limit)


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    return crud.get_product_by_id(product_id)


@router.post("/", response_model=ProductOut)
def create_product(product: ProductIn, current_user: UserOut = Depends(get_current_user)):
    product_id = crud.create_product(product.dict())
    return crud.get_product_by_id(product_id)
