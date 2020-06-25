from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.schemas.sellers import SellerOut, SellerToInsert, SellerToUpdate
from mpapi.schemas.users import UserOut
from mpapi.crud.sellers import Sellers
from mpapi.crud.users import Users

from ._exceptions import bad_request, not_found
from ._security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[SellerOut])
async def get_sellers(skip: int = 0, limit: int = 100):
    try:
        return Sellers.get_many(skip, limit)
    except:
        raise bad_request()


@router.get("/{seller_id}", response_model=SellerOut)
def get_seller_by_id(seller_id: str = Path(..., title="The seller ID as a valid ObjectId")):
    try:
        seller = Sellers.get_one(seller_id)
        if not(seller): raise
        return seller
    except:
        raise not_found()


@router.post("/", response_model=SellerOut, status_code=201)
def create_seller(Seller: SellerToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    try:
        seller_id = Sellers.create_one(Seller)
        if seller_id:
            if not(hasattr(CurrentUser, 'sellerId')) or CurrentUser.sellerId is None:
                Users.update_one(CurrentUser.id, {"sellerId": seller_id})
            return Sellers.get_one(seller_id)
    except Exception as e:
        raise bad_request(e)


@router.put("/{seller_id}", response_model=SellerOut)
def update_seller(
    *,
    seller_id: str = Path(..., title="The seller ID as a valid ObjectId"),
    Seller: SellerToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    try:
        Sellers.update_one(seller_id, Seller)
        return Sellers.get_one(seller_id)
    except Exception as e:
        raise bad_request(e)


@router.delete("/{seller_id}", status_code=204)
def delete_seller(seller_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    try:
        Sellers.delete_one(seller_id)
    except Exception as e:
        raise bad_request(e)
