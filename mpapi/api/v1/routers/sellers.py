from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.schemas.sellers import SellerOut, SellerToInsert, SellerToUpdate
from mpapi.schemas.users import UserOut
from mpapi.crud.sellers import Sellers
from mpapi.crud.users import Users

from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[SellerOut])
async def get_sellers(skip: int = 0, limit: int = 100):
    return format_result(Sellers.get_many(skip, limit))


@router.get("/{seller_id}", response_model=SellerOut)
def get_seller_by_id(seller_id: str = Path(..., title="The seller ID as a valid ObjectId")):
    return format_result(Sellers.get_one(seller_id))


@router.post("/", response_model=SellerOut, status_code=201)
def create_seller(Seller: SellerToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    result = Sellers.create_one(Seller)
    if result['success'] and result['value']:
        seller_id = result['value']
        if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
            Users.update_one(CurrentUser.id, {"sellerId": seller_id})
    return format_result(result)


@router.put("/{seller_id}", response_model=SellerOut)
def update_seller(
    *,
    seller_id: str = Path(..., title="The seller ID as a valid ObjectId"),
    Seller: SellerToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    return format_result(Sellers.update_one(seller_id, Seller))


@router.delete("/{seller_id}", status_code=204)
def delete_seller(seller_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(Sellers.delete_one(seller_id))
