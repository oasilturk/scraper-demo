from pymongo import MongoClient
import config

class Database:
    def __init__(self):
        self.client = MongoClient(config.CONN_URI)
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]

    def get_collection(self):
        return self.collection
