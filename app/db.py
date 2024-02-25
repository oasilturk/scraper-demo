from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "test_database"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def insert_test_data():
    collection = db["test_collection"]
    test_data = {"name": "test", "value": 123}
    result = collection.insert_one(test_data)
    return result.inserted_id