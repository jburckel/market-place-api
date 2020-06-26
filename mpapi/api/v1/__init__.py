from fastapi import APIRouter

from .routers import products, product_attributes, product_attribute_values, product_categories, orders, sellers, users

router = APIRouter()


router.include_router(
    products.router,
    prefix='/products',
    tags=['products']
)


router.include_router(
    product_attributes.router,
    prefix='/product-attributes',
    tags=['product-attributes']
)


router.include_router(
    product_attribute_values.router,
    prefix='/product-attribute-values',
    tags=['product-attribute-values']
)


router.include_router(
    product_categories.router,
    prefix='/product-categories',
    tags=['product-categories']
)


router.include_router(
    orders.router,
    prefix='/orders',
    tags=['orders']
)


router.include_router(
    sellers.router,
    prefix='/sellers',
    tags=['sellers']
)



router.include_router(
    users.router,
    prefix='/users',
    tags=['users']
)
