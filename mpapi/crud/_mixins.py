from pymongo.collection import Collection
from pydantic.main import ModelMetaclass

from fastapi import HTTPException

from mpapi.core.database import get_collection
from mpapi.core.collection import COLLECTIONS

from mpapi.schemas.exceptions import Exceptions

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


    @staticmethod
    def format_result(result: tuple):
        success = result[0]
        value = result[1]
        error_id = result[2]
        return {'success': result[0], 'value': value, 'error': error_id}


    def get_one(self, id: str = None, query: dict = None) -> dict:
        if id is not None:
            return self.format_result(find_one_by_id(self.collection, id))
        elif query is not None:
            return self.format_result(find_one_by_query(self.collection, query))
        else:
            return self.format_result((False, None, Exceptions.GET_BAD_REQUEST))


    def get_many(
        self,
        skip: int = 0,
        limit: int = 0,
        filters: dict = None
    ) -> list:
        try:
            return self.format_result(
                (
                    True,
                    [item for item in self.collection.find(filters).skip(skip).limit(limit)],
                    None

                )
            )
        except Exception:
            return self.format_result((False, None, Exceptions.GET_BAD_REQUEST))


    def create_one(self, item) -> str:
        ItemValidated = self.validate_fields(item, self.CreateValidation)
        if ItemValidated is not None:
            try:
                result = insert_one(self.collection, self.to_dict(ItemValidated, exclude_unset=False))
                if result[0] is not True:
                    return self.format_result(result)
                else:
                    return self.get_one(result[1])
            except Exception as e:
                return self.format_result((False, None, Exceptions.CREATE_UNKNOWN))
        return self.format_result((False, None, Exceptions.CREATE_BAD_REQUEST))


    def create_many(self, items: list) -> list:
        return


    def update_one(self, id: str, item, fields_to_exclude: set = set()):
        ItemValidated = self.validate_fields(item, self.UpdateValidation)
        if ItemValidated is not None:
            result = update_one_by_id(self.collection, id, self.to_dict(ItemValidated, fields_to_exclude, True))
            if result[0] is not True:
                return self.format_result(result)
            else:
                return self.get_one(id)
        return self.format_result((False, None, Exceptions.UPDATE_BAD_REQUEST))


    def update_many(self, items: list):
        return


    def delete_one(self, id: str):
        try:
            return self.format_result(delete_one_by_id(self.collection, id))
        except Exception as e:
            return self.format_result(False, None, Exceptions.DELETE_BAD_REQUEST)


    def delete_many(self, items: list):
        return
