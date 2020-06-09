from pymongo import MongoClient, errors

from mpapi import settings
from .collection import create_collections

serverTimeout = 2000

try:
    if not(settings.DATABASE_USERNAME):
        client = MongoClient(settings.DATABASE_URI, serverSelectionTimeoutMS = serverTimeout)
    else:
        client = MongoClient(
            settings.DATABASE_URI,
            username = settings.DATABASE_USERNAME,
            password = settings.DATABASE_PASSWORD,
            authSource = settings.DATABASE_AUTHSOURCE,
            authMechanism = settings.DATABASE_AUTHMECHANISM,
            servertSelectionTimeoutMS = serverTimeout
        )

    info = client.server_info()
except errors.ServerSelectionTimeoutError as error:
    print("Could not connect to Database. ERROR:", error)

try:
    db = client[settings.DATABASE_NAME]
except AttributeError as error:
    print("Get MongoDB database ERROR:", error)

if settings.DATABASE_NAME not in client.list_database_names():
    print('Creating collections')
    create_collections(db)

def get_collection(collection: str):
    try:
        MongoDBCollection = db[collection]
    except AttributeError as error:
        print("Get MongoDB collection ERROR:", error)
    return MongoDBCollection
