from pymongo import MongoClient

from mpapi import settings

client = MongoClient(settings.DATABASE_URI)

db = client[settings.DATABASE_NAME]
