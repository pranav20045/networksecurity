import pymongo
import certifi
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

try:
    client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=certifi.where())
    print("Connected:", client.list_database_names())
except Exception as e:
    print("Connection failed:", e)
