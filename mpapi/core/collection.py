from pymongo import ASCENDING

COLLECTIONS = {
    "PRODUCTS": "products",
    "USERS": "users"
}

def create_collections(db):

    products = db.create_collection(COLLECTIONS["PRODUCTS"])
    products.create_index([('code', ASCENDING)], unique=True)

    users = db.create_collection(COLLECTIONS["USERS"])
    users.create_index([('username', ASCENDING)], unique=True)
