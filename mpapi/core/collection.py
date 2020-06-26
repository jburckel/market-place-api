from pymongo import ASCENDING

COLLECTIONS = {
    "PRODUCTS": "products",
    "PRODUCT-ATTRIBUTES": "product-attributes",
    "PRODUCT-ATTRIBUTE-VALUES": "product-attribute-values",
    "PRODUCT-CATEGORIES": "product-categories",
    "USERS": "users",
    "SELLERS": "sellers",
    "ORDERS": "orders"
}

def create_collections(db):

    products = db.create_collection(COLLECTIONS["PRODUCTS"])
    products.create_index([('sku', ASCENDING)])
    products.create_index([('productModelId', ASCENDING)])

    users = db.create_collection(COLLECTIONS["USERS"])
    users.create_index([('username', ASCENDING)], unique=True)

    sellers = db.create_collection(COLLECTIONS["SELLERS"])

    product_attributes = db.create_collection(COLLECTIONS["PRODUCT-ATTRIBUTES"])

    product_attribute_values = db.create_collection(COLLECTIONS["PRODUCT-ATTRIBUTE-VALUES"])

    product_categories = db.create_collection(COLLECTIONS["PRODUCT-CATEGORIES"])
