from pymongo import MongoClient, errors

from mpapi import settings

from .collection import create_collections

try:
    if not(settings.DATABASE_USERNAME):
        client = MongoClient(settings.DATABASE_URI, serverSelectionTimeoutMS = settings.DATABASE_TIMEOUT)
    else:
        client = MongoClient(
            settings.DATABASE_URI,
            username = settings.DATABASE_USERNAME,
            password = settings.DATABASE_PASSWORD,
            authSource = settings.DATABASE_AUTHSOURCE,
            authMechanism = settings.DATABASE_AUTHMECHANISM,
            servertSelectionTimeoutMS = settings.SERVER_TIMEOUT
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
