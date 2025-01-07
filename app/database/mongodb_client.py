# app/database/mongodb_client.py
from pymongo import MongoClient
from app.utils.config import MONGODB_URI

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client.cloudwithdevesh
        
    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def close(self):
        self.client.close()

# Initialize database connection
db = MongoDB()