from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.orders import Orders
from mpapi.schemas.users import UserOut
from mpapi.schemas.orders import OrderToInsert, OrderToUpdate, OrderOut

from ._security import get_current_user
from ._utils import format_result

router = APIRouter()

@router.get("/", response_model=List[OrderOut])
async def get_orders(skip: int = 0, limit: int = 100):
    return format_result(Orders.get_many(skip, limit))


@router.get("/{order_id}", response_model=OrderOut)
def get_order_by_id(order_id: str = Path(..., title="The order ID as a valid ObjectId")):
    return format_result(Orders.get_one(order_id))


@router.post("/", response_model=OrderOut, status_code=201)
def create_order(Order: OrderToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    Order.userId = CurrentUser.id
    return format_result(Orders.create_one(Order))


@router.put("/{order_id}", response_model=OrderOut)
def update_order(
    *,
    order_id: str = Path(..., title="The order ID as a valid ObjectId"),
    Order: OrderToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    # Exclude userId and sellerId because it seems there is no reason to update them
    return format_result(Orders.update_one(order_id, Order, {'userId', 'sellerId'}))


@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    return format_result(Orders.delete_one(order_id))
