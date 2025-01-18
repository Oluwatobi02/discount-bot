import os
from pymongo.mongo_client import MongoClient
from pymongo.cursor import Cursor
from bson import json_util
from json import loads
from dotenv import load_dotenv
load_dotenv("shared.env")
from app.product import Product
class Database:
    __instance = None
    connected = False
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls)
            cls.__instance.connection = None
        return cls.__instance

    def connect(self):
        if self.connection is None:
            self.url = os.getenv("MONGO_URL")
            client = MongoClient(self.url)
            db = client["discountbot"]
            self.connection = db 
            self.connected = True
            return self

    def disconnect(self):
        if self.connection is not None:
            self.connection = None
            self.connected = False
            self.url = None
        return self
    
    def create_collections(self):
        if self.connected:
            db = self.connection
            try:
                db.create_collection("products")
            except Exception as e:
                print(e)
            try:
                db.create_collection("users")
            except Exception as e:
                print(e)
            return self
        return None

    def insert_product(self, product: Product):
        if self.connected:
            collection = self.connection["products"]
            collection.insert_one(product.to_dict())
        return False
    
    def get_products(self):
        if self.connected:
            collection = self.connection["products"]
            db_products : Cursor = collection.find()
            return loads(json_util.dumps(list(db_products)))
        return None