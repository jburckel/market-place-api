from fastapi import APIRouter

from .routers import products

router = APIRouter()

router.include_router(
    products.router,
    prefix="/products"
)
