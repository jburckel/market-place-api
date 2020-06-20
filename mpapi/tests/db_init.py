import sys
import re

from pymongo import MongoClient, errors

from mpapi.crud.sellers import Sellers
from mpapi.crud.users import Users

def db_drop(database_uri, database_name):
    try:
        MongoClient(database_uri).drop_database(database_name)
    except Exception:
        print('Not able to drop database')
        pass


def db_init(database_uri, database_name, delete=False):
    if delete:
        db_drop(database_uri, database_name)
    Users.create_one({"username": "johndoe", "email": "johndoe@mail.com", "password": "@@123456Abc**"})
    Sellers.create_one({"name": "Company1"})
