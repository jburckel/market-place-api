from fastapi import APIRouter

from .routers import products, users

router = APIRouter()

router.include_router(
    products.router,
    prefix="/products",
    tags=['products']
)

router.include_router(
    users.router,
    prefix="/users",
    tags=['users']
)
