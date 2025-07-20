import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  
def get_database():
    mongo_uri = os.getenv("MONGODB_URI")
    print("Connecting to MongoDB URI:", mongo_uri)
    client = MongoClient(mongo_uri)
    db = client["ecommerce_db"]
    print("Using database:", db.name)
    return db

def get_product_collection():
    return get_database()["products"]

def get_order_collection():
    return get_database()["orders"]





