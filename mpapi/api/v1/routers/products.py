from fastapi import APIRouter, HTTPException, Path
from typing import List
from bson import ObjectId, errors

from mpapi.database import db
from mpapi.schemas.products import ProductCreate, Product

router = APIRouter()

products = db.products

@router.get("/", response_model=List[Product])
async def get_products(skip: int = 0, limit: int = 100):
    catalog = []
    for product in products.find().skip(skip).limit(limit):
        catalog.append(product)
    return catalog


@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: str = Path(..., title="The product ID as a valid ObjectId")):
    try:
        product = products.find_one({'_id': ObjectId(product_id)})
    except errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Product Id")
    if not(product):
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product)
def get_product_by_id(product: ProductCreate):
    try:
        product_id = products.insert_one(product.dict()).inserted_id
        db_product = products.find_one({'_id': ObjectId(product_id)})
    except:
        raise HTTPException(status_code=500, detail="Error inserting new product")
    return db_product
