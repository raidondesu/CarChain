import pymongo
import os
from dotenv import load_dotenv

class DBConnect:
    
    """
    Connects to MongoDB database; has two methods:
    1. to ingest a block 
    2. to query documents according to car_id
    """
    
    def __init__(self):
        
        load_dotenv()
        self.USER_NAME = os.getenv("USER_NAME")
        self.PASSWORD = os.getenv("PASSWORD")
        self.DATA_BASE = os.getenv("DATA_BASE")
        mongo_client = pymongo.MongoClient(
            f"mongodb+srv://{self.USER_NAME}:{self.PASSWORD}@cluster0.e1xus.mongodb.net/{self.DATA_BASE}?retryWrites=true&w=majority")
        db = mongo_client.CarChain
        self.storage = db.CarChainStorage
        
    def ingest_block(self, block):
        
        self.storage.insert(block)
        
       
    def get_car_history(self, car_id):
    
        """
        method to query all entries in data base of a given car_id
        
        error handling for unknown key is still missing
        """
        return sorted([item for item in self.storage.find({"car_id":car_id})], key = lambda i: i["_id"])
        
        