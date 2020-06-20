from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.schemas.sellers import SellerOut, SellerToInsert, SellerToUpdate
from mpapi.schemas.users import UserOut
from mpapi.crud.sellers import Sellers
from mpapi.crud.users import get_current_user

router = APIRouter()

@router.get("/", response_model=List[SellerOut])
async def get_sellers(skip: int = 0, limit: int = 100):
    return Sellers.get_many(skip, limit)


@router.get("/{seller_id}", response_model=SellerOut)
def get_seller_by_id(seller_id: str = Path(..., title="The seller ID as a valid ObjectId")):
    return Sellers.get_one(seller_id)


@router.post("/", response_model=SellerOut, status_code=201)
def create_seller(seller: SellerToInsert, current_user: UserOut = Depends(get_current_user)):
    seller_id = Sellers.create_one(seller)
    return Sellers.get_one(seller_id)


@router.put("/{seller_id}", response_model=SellerOut)
def update_seller(
    *,
    seller_id: str = Path(..., title="The seller ID as a valid ObjectId"),
    seller: SellerToUpdate,
    current_user: UserOut = Depends(get_current_user)
):
    Sellers.update_one(seller_id, seller)
    return Sellers.get_one(seller_id)


@router.delete("/{seller_id}", status_code=204)
def delete_seller(seller_id: str, current_user: UserOut = Depends(get_current_user)):
    Sellers.delete_one(seller_id)
