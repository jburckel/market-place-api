from enum import IntEnum
from pydantic import BaseModel, Field
from typing List

from .commons import Address, ObjectIdStr
from .products import ProductBase

class OrderStatus(IntEnum):
    unconfirm = -1
    confirm = 0
    payed = 1
    preparing = 2
    shipped = 3
    delivered = 4
    complaint = 100
    refund = 101
    canceled = 1000


class OrderLineBase(BaseModel):
    product: ProductBase
    quantity: float
    basePrice: float
    discount: float = 0
    totalPrice: float


class OrderBase(BaseModel):
    userId: ObjectIdStr = None
    companyId: ObjectIdStr = None
    invoiceAddress: Address = None
    shippingAddress: Address = None
    totalPrice: float = None
    currencyId: str = None
    lines: List[OrderLineBase] = None
    status: OrderStatus = None


class OrderToInsert(OrderBase):
    userId: ObjectIdStr
    companyId: ObjectIdStr
    invoiceAddress: Address
    totalPrice: float
    currencyId: str
    lines: List[OrderLineBase]
    status: OrderStatus = OrderStatus.unconfirm


class OrderToUpdate(OrderBase):
    pass


class OrderOut(DBModel, OrderBase):
    pass
