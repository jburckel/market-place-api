from bson import ObjectId, errors as bson_errors
from pymongo import errors as pymongo_errors
from pymongo.collection import Collection

from fastapi import HTTPException

from mpapi.schemas.exceptions import Exceptions

def get_collection_name(collection: Collection):
    collection_name = collection.name
    return collection_name[:-1].title() if collection_name[-1] == 's' else collection_name.title()


def find_one_by_id(collection: Collection, id: str) -> dict:
    """
        Retrieve a object of a collection with the id provided.
    """
    object_name = get_collection_name(collection)
    try:
        object = collection.find_one({'_id': ObjectId(id)})
    except bson_errors.InvalidId:
        return False, None, Exceptions.INVALID_OBJECT_ID
    except Exception:
        return False, None, Exceptions.GET_UNKNOWN
    if not(object):
        return False, None, Exceptions.GET_NOT_FOUND
    return True, object, None


def find_one_by_query(collection: Collection, query: dict) -> dict:
    """
        Retrieve a object of a collection with the value provided.
    """
    object_name = get_collection_name(collection)
    try:
        object = collection.find_one(query)
    except:
        return False, None, Exceptions.GET_UNKNOWN
    if not(object):
        return False, None, Exceptions.GET_NOT_FOUND
    return True, object, None


def insert_one(collection: Collection, values_to_insert: dict) -> str:
    id = ''
    try:
        id = collection.insert_one(values_to_insert).inserted_id
    except pymongo_errors.DuplicateKeyError as err:
        return False, None, Exceptions.CREATE_DUPLICATE_KEY
    except Exception:
        return False, None, Exceptions.CREATE_UNKNOWN
    return True, id, None


def update_one_by_id(collection: Collection, id: str, values_to_update: dict):
    object_name = get_collection_name(collection)
    try:
        collection.update_one({'_id': ObjectId(id)}, {'$set': values_to_update})
    except Exception as err:
        return False, None, Exceptions.UPDATE_UNKNOWN
    return True, id, None


def delete_one_by_id(collection: Collection, id: str):
    object_name = get_collection_name(collection)
    try:
        collection.delete_one({'_id': ObjectId(id)})
    except Exception as err:
        return False, None, Exceptions.DELETE_UNKNOWN
    return True, id, None
