from typing import List

from fastapi import APIRouter, Path, Depends

from mpapi.crud.product_categories import ProductCategories
from mpapi.schemas.users import UserOut
from mpapi.schemas.product_categories import ProductCategoryToInsert, ProductCategoryToUpdate, ProductCategoryOut

from ._exceptions import mpapi_exceptions
from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[ProductCategoryOut])
async def get_product_categories(skip: int = 0, limit: int = 100):
    return format_result(ProductCategories.get_many(skip, limit))


@router.get("/{product_category_id}", response_model=ProductCategoryOut)
def get_product_category_by_id(product_category_id: str = Path(..., title="The product category ID as a valid ObjectId")):
    return format_result(ProductCategories.get_one(product_category_id))


@router.post("/", response_model=ProductCategoryOut, status_code=201)
def create_product_category(ProductCategory: ProductCategoryToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
        raise mpapi_exceptions({'error': 'USER-HAS-NO-SELLERID'})
    ProductCategory.sellerId = CurrentUser.sellerId
    return format_result(ProductCategories.create_one(ProductCategory))


@router.put("/{product_category_id}", response_model=ProductCategoryOut)
def update_product_category(
    *,
    product_category_id: str = Path(..., title="The product_category ID as a valid ObjectId"),
    ProductCategory: ProductCategoryToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    # Exclude sellerId because it seems there is no reason to update it
    return format_result(ProductCategories.update_one(product_category_id, ProductCategory, {'sellerId'}))


@router.delete("/{product_category_id}", status_code=204)
def delete_product_category(product_category_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(ProductCategories.delete_one(product_category_id))
