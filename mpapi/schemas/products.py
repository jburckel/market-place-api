from pydantic import BaseModel
from .mixins import DBModel

class ProductCreate(BaseModel):
    code: str
    description: str = None

class Product(DBModel, ProductCreate):
    pass
