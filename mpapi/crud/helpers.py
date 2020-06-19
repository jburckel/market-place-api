from bson import ObjectId, errors as bson_errors
from pymongo import errors as pymongo_errors
from pymongo.collection import Collection

from fastapi import HTTPException

def get_collection_name(collection: Collection):
    collection_name = collection.name
    return collection_name[:-1].title() if collection_name[-1] == 's' else collection_name.title()


def find_one_by_id(collection: Collection, id: str) -> dict:
    """
        Retrieve a object of a collection with the id provided
        The function verify that the id is a correct ObjectId, if not it returns 400 error
        If nothing is found in DB, it returns 404 error
    """
    object_name = get_collection_name(collection)
    try:
        object = collection.find_one({'_id': ObjectId(id)})
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail=f"Invalid {object_name} Id")
    if not(object):
        raise HTTPException(status_code=404, detail=f"{object_name} not found")
    return object


def find_one_by_value(collection: Collection, value_name: str, value) -> dict:
    """
        Retrieve a object of a collection with the value provided
        If nothing is found in DB, it returns 404 error
    """
    object_name = get_collection_name(collection)
    object = collection.find_one({value_name: value})
    if not(object):
        raise HTTPException(status_code=404, detail=f"{object_name} not found")
    return object


def insert_one(collection: Collection, values_to_insert: dict) -> str:
    id = ''
    try:
        id = collection.insert_one(values_to_insert).inserted_id
    except pymongo_errors.DuplicateKeyError as err:
        raise HTTPException(status_code=400, detail=f"Duplicate value. ERROR: {err}")
    return id


def update_one_by_id(collection: Collection, id: str, values_to_update: dict):
    object_name = get_collection_name(collection)
    try:
        collection.update_one({'_id': ObjectId(id)}, {'$set': values_to_update})
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Update {object_name} error. ERROR: {err}")


def delete_one_by_id(collection: Collection, id: str):
    object_name = get_collection_name(collection)
    try:
        collection.delete_one({'_id': ObjectId(id)})
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Delete {object_name} error. ERROR: {err}")
