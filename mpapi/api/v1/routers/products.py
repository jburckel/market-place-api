from fastapi import APIRouter, HTTPException, Path, Depends
from typing import List
from bson import ObjectId, errors

from mpapi.core.database import get_collection
import mpapi.crud.products as crud
from mpapi.crud.users import get_current_user
from mpapi.schemas.users import User
from mpapi.schemas.products import ProductCreate, Product

router = APIRouter()

products = get_collection("products")

@router.get("/", response_model=List[Product])
async def get_products(skip: int = 0, limit: int = 100):
    return crud.get_products(skip, limit)


@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    return crud.get_product_by_id(product_id)


@router.post("/", response_model=Product)
def create_product(product: ProductCreate, current_user: User = Depends(get_current_user)):
    product_id = crud.create_product(product.dict())
    return crud.get_product_by_id(product_id)
