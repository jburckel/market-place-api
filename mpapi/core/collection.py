from pymongo import ASCENDING

COLLECTIONS = {
    "PRODUCTS": "products",
    "USERS": "users",
    "SELLERS": "sellers"
}

def create_collections(db):

    products = db.create_collection(COLLECTIONS["PRODUCTS"])
    products.create_index([('sku', ASCENDING)])
    products.create_index([('productModelId', ASCENDING)])

    users = db.create_collection(COLLECTIONS["USERS"])
    users.create_index([('username', ASCENDING)], unique=True)

    sellers = db.create_collection(COLLECTIONS["SELLERS"])
