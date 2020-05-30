from fastapi import APIRouter

router = APIRouter()

test_products = [
    {"code": "ABC", "description": "Awesome product"},
    {"code": "DEF", "description": "Bad product"},
    {"code": "GHI", "description": "Good product"},
]


@router.get("/")
async def get_products(skip: int = 0, limit: int = 10):
    return test_products[skip:limit]


@router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    if len(test_products) > product_id:
        return test_products[product_id]
    return {}
