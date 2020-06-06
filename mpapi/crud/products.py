from bson import ObjectId

from fastapi import HTTPException

from mpapi.core.database import get_collection

products = get_collection("products")

def get_product(product_id: str):
    
