import os

CONN_URI = (
    "mongodb://<your_db_user>:<your_db_password>@localhost:27017/<your_database_name>"
)
DB_NAME = "scraper_demo_db"
COLLECTION_NAME = "products"
XML_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lonca-sample.xml")