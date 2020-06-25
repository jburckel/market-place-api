from mpapi.schemas.sellers import SellerToInsert, SellerToUpdate

from ._mixins import BaseCrud

class SellersCrud(BaseCrud):
    pass

Sellers = SellersCrud("SELLERS", SellerToInsert, SellerToUpdate)
