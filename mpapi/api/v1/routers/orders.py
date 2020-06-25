from fastapi import APIRouter, Path, Depends
from typing import List

from mpapi.crud.orders import Orders
from mpapi.schemas.users import UserOut
from mpapi.schemas.orders import OrderToInsert, OrderToUpdate, OrderOut

from ._exceptions import bad_request, not_found
from ._security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[OrderOut])
async def get_orders(skip: int = 0, limit: int = 100):
    try:
        return Orders.get_many(skip, limit)
    except Exception:
        raise bad_request()



@router.get("/{order_id}", response_model=OrderOut)
def get_order_by_id(order_id: str = Path(..., title="The order ID as a valid ObjectId")):
    try:
        order = Orders.get_one(order_id)
        if not(order): raise
        return order
    except Exception:
        raise not_found()


@router.post("/", response_model=OrderOut, status_code=201)
def create_order(Order: OrderToInsert, CurrentUser: UserOut = Depends(get_current_user)):
    Order.userId = CurrentUser.id
    try:
        order_id = Orders.create_one(Order)
        return Orders.get_one(order_id)
    except Exception as e:
        raise bad_request(e)


@router.put("/{order_id}", response_model=OrderOut)
def update_order(
    *,
    order_id: str = Path(..., title="The order ID as a valid ObjectId"),
    Order: OrderToUpdate,
    CurrentUser: UserOut = Depends(get_current_user)
):
    try:
        # Exclude userId and sellerId because it seems there is no reason to update them
        Orders.update_one(order_id, Order, {'userId', 'sellerId'})
        return Orders.get_one(order_id)
    except Exception as e:
        raise bad_request(e)



@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: str, CurrentUser: UserOut = Depends(get_current_user)):
    try:
        Orders.delete_one(order_id)
    except Exception as e:
        raise bad_request(e)
