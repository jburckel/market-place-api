from pymongo.collection import Collection
from pydantic.main import ModelMetaclass

from fastapi import HTTPException

from mpapi.core.database import get_collection
from mpapi.core.collection import COLLECTIONS

from .helpers import find_one_by_id, find_one_by_query, insert_one, update_one_by_id, delete_one_by_id

class BaseCrud:

    def __init__(
        self,
        collection: Collection,
        CreateValidation: ModelMetaclass,
        UpdateValidation: ModelMetaclass
    ):
        self.collection = get_collection(COLLECTIONS[collection])
        self.CreateValidation = CreateValidation
        self.UpdateValidation = UpdateValidation

    def get_one(self, id: str = None, query: dict = None) -> dict:
        if id is not None:
            return find_one_by_id(self.collection, id)
        elif query is not None:
            return find_one_by_query(self.collection, query)
        else:
            return {}

    def get_many(
        self,
        skip: int = 0,
        limit: int = 0,
        filters: dict = None
    ) -> list:
        return [item for item in self.collection.find(filters).skip(skip).limit(limit)]

    def create_one(self, item) -> str:
        if isinstance(item, self.CreateValidation):
            return insert_one(self.collection, item.dict())
        elif type(item) == ModelMetaclass:
            item_validated = self.CreateValidation(**item.dict())
            return insert_one(self.collection, item_validated.dict())
        elif type(item) == dict:
            item_validated = self.CreateValidation(**item)
            return insert_one(self.collection, item_validated.dict())
        else:
            raise HTTPException(
                status_code=400,
                detail="Bad request",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def create_many(self, items: list) -> list:
        return

    def update_one(self, id: str, item: dict):
        item_validated = None
        if isinstance(item, self.UpdateValidation):
            item_validated = item
        elif type(item) == ModelMetaclass:
            item_validated = self.CreateValidation(**item.dict())
        elif type(item) == dict:
            item_validated = self.CreateValidation(**item)
        if item_validated is not None:
            update_one_by_id(self.collection, id, item_validated.dict(exclude_unset=True))
        else:
            raise HTTPException(
                status_code=400,
                detail="Bad request",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def update_many(self, items: list):
        return

    def delete_one(self, id: str):
        delete_one_by_id(self.collection, id)

    def delete_many(self, items: list):
        return
