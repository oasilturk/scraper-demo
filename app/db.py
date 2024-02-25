from pymongo import MongoClient
import config

client = MongoClient(config.CONN_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]

def insert_test_data():
    test_data = {"name": "test", "value": 123}
    result = collection.insert_one(test_data)
    return result.inserted_id