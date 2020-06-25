from mpapi.schemas.orders import OrderToInsert, OrderToUpdate

from ._mixins import BaseCrud

class OrdersCrud(BaseCrud):
    pass

Orders = OrdersCrud("ORDERS", OrderToInsert, OrderToUpdate)
