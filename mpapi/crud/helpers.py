from bson import ObjectId, errors as bson_errors
from pymongo import errors as pymongo_errors

from fastapi import HTTPException


def find_one_by_id(collection, id: str):
    """
        Retrieve a object of a collection with the id provided
        The function verify that the id is a correct ObjectId, if not it returns 400 error
        If nothing is found in DB, it returns 404 error
    """
    collection_name = collection.name
    object_name = collection_name[:-1].title() if collection_name[-1] == 's' else collection_name.title()
    try:
        object = collection.find_one({'_id': ObjectId(id)})
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail=f"Invalid {object_name} Id")
    if not(object):
        raise HTTPException(status_code=404, detail=f"{object_name} not found")
    return object


def find_one_by_value(collection, value_name: str, value):
    """
        Retrieve a object of a collection with the value provided
        If nothing is found in DB, it returns 404 error
    """
    collection_name = collection.name
    object_name = collection_name[:-1].title() if collection_name[-1] == 's' else collection_name.title()
    object = collection.find_one({value_name: value})
    if not(object):
        raise HTTPException(status_code=404, detail=f"{object_name} not found")
    return object

def insert_one(collection, values: dict):
    try:
        return collection.insert_one(values).inserted_id
    except pymongo_errors.DuplicateKeyError as err:
        raise HTTPException(status_code=400, detail=f"Duplicate value. ERROR: {err}")
