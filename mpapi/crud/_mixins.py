from pymongo.collection import Collection
from pydantic.main import ModelMetaclass

from fastapi import HTTPException

from mpapi.core.database import get_collection
from mpapi.core.collection import COLLECTIONS

from ._exceptions import MPAPIException
from ._helpers import find_one_by_id, find_one_by_query, insert_one, update_one_by_id, delete_one_by_id

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

    @staticmethod
    def validate_fields(item, ValidationClass: ModelMetaclass):
        ItemValidated = None
        if isinstance(item, ValidationClass):
            ItemValidated = item
        elif type(item) == ModelMetaclass:
            ItemValidated = ValidationClass(**item.dict())
        elif type(item) == dict:
            ItemValidated = ValidationClass(**item)
        if ItemValidated is not None:
            return ItemValidated
        return None


    @staticmethod
    def to_dict(Item, fields_to_exclude: set = set(), exclude_unset: bool = False):
        return Item.dict(exclude=fields_to_exclude, exclude_unset=exclude_unset)


    def get_one(self, id: str = None, query: dict = None) -> dict:
        if id is not None:
            try:
                return find_one_by_id(self.collection, id)
            except Exception as e:
                raise MPAPIException(e)

        elif query is not None:
            try:
                return find_one_by_query(self.collection, query)
            except Exception as e:
                raise MPAPIException(e)
        else:
            raise MPAPIException("No result")


    def get_many(
        self,
        skip: int = 0,
        limit: int = 0,
        filters: dict = None
    ) -> list:
        return [item for item in self.collection.find(filters).skip(skip).limit(limit)]


    def create_one(self, item) -> str:
        ItemValidated = self.validate_fields(item, self.CreateValidation)
        if ItemValidated is not None:
            try:
                return insert_one(self.collection, self.to_dict(ItemValidated, exclude_unset=False))
            except Exception as e:
                raise MPAPIException(e)
        else:
            raise MPAPIException(f"Invalid data")


    def create_many(self, items: list) -> list:
        return


    def update_one(self, id: str, item, fields_to_exclude: set = set()):
        ItemValidated = self.validate_fields(item, self.UpdateValidation, )
        if ItemValidated is not None:
            try:
                return update_one_by_id(self.collection, id, self.to_dict(ItemValidated, fields_to_exclude, True))
            except Exception as e:
                raise MPAPIException(e)
        raise MPAPIException(f"Invalid data")


    def update_many(self, items: list):
        return


    def delete_one(self, id: str):
        if id is None:
            raise MPAPIException("Id can not be null")
        try:
            return delete_one_by_id(self.collection, id)
        except Exception as e:
            raise MPAPIException(e)


    def delete_many(self, items: list):
        return
