from pydantic import BaseModel
from typing import List, Optional

from .mixins import DBModel
from .commons import MultiLanguageText, Image

class ProductImage(Image):
    main: bool = False

class ProductBase(BaseModel):
    code: str
    price: float = 0
    currency: Optional[str] = None
    name: MultiLanguageText = None
    short_description: Optional[MultiLanguageText] = None
    description: Optional[MultiLanguageText] = None
    images: Optional[List[ProductImage]] = None

class ProductIn(ProductBase):
    pass

class ProductOut(DBModel, ProductBase):
    pass

class ProductInDB(ProductBase):
    pass

class ProductOutDB(ProductBase):
    pass
