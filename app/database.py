from pymongo import MongoClient
import config
import logging


class Database:
    def __init__(self):
        logging.info("Initializing database connection")
        self.client = MongoClient(config.CONN_URI)
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        logging.info("Database connection established")

    def get_collection(self):
        return self.collection
