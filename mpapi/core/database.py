from pymongo import MongoClient

from mpapi import settings

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
except:
    print("Connection error")

try:
    db = client[settings.DATABASE_NAME]
except AttributeError as error:
    print("Get MongoDB database ERROR:", error)

def get_collection(collection: str):
    try:
        MongoDBCollection = db[collection]
    except AttributeError as error:
        print("Get MongoDB collection ERROR:", error)
    return MongoDBCollection
