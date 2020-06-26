from bson import ObjectId

from enum import IntEnum
from pydantic import BaseModel, Field
from typing import List

from ._commons import Address, ObjectIdStr
from ._mixins import DBModel
from .products import ProductOut

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
    product: ProductOut = None
    quantity: float = None
    basePrice: float = None
    discount: float = None
    totalPrice: float = None


class OrderBase(BaseModel):
    userId: ObjectIdStr = None
    sellerId: ObjectIdStr = None
    invoiceAddress: Address = None
    shippingAddress: Address = None
    totalPrice: float = None
    currencyId: str = None
    lines: List[OrderLineBase] = None
    status: OrderStatus = None

    class Config:
        schema_extra = {
            'example': {
                'userId': str(ObjectId()),
                'sellerId': str(ObjectId()),
                'invoiceAddress': {
                    'name': None,
                    'addressLine1': '1 rue de la paix',
                    'addressLine2': None,
                    'postalCode': 75000,
                    'town': 'Paris',
                    'state': None,
                    'country': 'France'

                },
                'shippingAddress': None,
                'totalPrice': 124.6,
                'currencyId': 'EUR',
                'lines': [
                    {
                        """
                        'product': {
                            '_id': str(ObjectId()),
                            'name': 'Test Product'
                        },
                        """
                        'quantity': 10,
                        'basePrice': 12.46,
                        'discount': 0,
                        'totalPrice': 124.6
                    }
                ],
                'status': 0
            }
        }


class OrderToInsert(OrderBase):
    userId: ObjectIdStr
    sellerId: ObjectIdStr
    invoiceAddress: Address
    totalPrice: float
    currencyId: str
    lines: List[OrderLineBase]
    status: OrderStatus = OrderStatus.unconfirm


class OrderToUpdate(OrderBase):
    pass


class OrderOut(DBModel, OrderBase):
    pass
