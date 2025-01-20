import os
from pymongo.mongo_client import MongoClient
from pymongo.cursor import Cursor
from dotenv import load_dotenv
load_dotenv("shared.env")
from app.builders.user_builder import UserBuilder
from app.builders.product_builder import ProductBuilder
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

    def insert_product(self, product):
        if self.connected:
            collection = self.connection["products"]
            collection.insert_one(product.to_dict())
        return False
    
    def get_product(self, id, **kwargs):
        if self.connected:
            collection = self.connection["products"]
            db_product = collection.find_one({"_id": id})
            return self.build_product(db_product)
        
    def get_products(self, skip):
        if self.connected:
            collection = self.connection["products"]
            db_products : Cursor = collection.find().skip(skip).limit(10)
            products = list(db_products)
            products = [self.build_product(product) for product in products]
            return products
        return None
    def build_product(self, product):
        item = ProductBuilder()\
                            .add_id(product["_id"])\
                            .add_name(product["name"])\
                            .add_price(product["price"])\
                            .add_original_price(product["original_price"])\
                            .add_currency(product["currency"])\
                            .add_discount(product["discount"])\
                            .add_product_condition(product["product_condition"])\
                            .add_link(product["link"])\
                            .add_image(product["image"])\
                            .build()
        
        for watcher in product.get("watchers", []):
            watcher = self.get_user(watcher)
            item.add_watcher(watcher)
        return item
    def build_user(self, user):
        user = UserBuilder()\
                            .add_email(user["email"])\
                            .add_name(user["name"])\
                            .add_phone(user["phone"])\
                            .add_password(user["password"])\
                            .add_watched_products(user.get("watched_products",[]))\
                            .build()
        return user
    
    def insert_user(self, user):
        if self.connected:
            collection = self.connection["users"]
            user = self.build_user(user)
            collection.insert_one(user.to_dict())
            return True
        return False
    
    def get_user(self, id):
        if self.connected:
            collection = self.connection["users"]
            db_user = collection.find_one({"_id": id})
            if db_user is not None:
                return self.build_user(db_user)
            return None
        return None
    
    def add_watcher_to_product(self, product_id, user_id):
        if self.connected:
            collection = self.connection["products"]
            collection.update_one({"_id": product_id}, {"$push": {"watchers": user_id}})
            collection = self.connection["users"]
            collection.update_one({"_id": user_id}, {"$push": {"watched_products": product_id}})
            return True
        return False
    def remove_watcher_from_product(self, product_id, user_id):
        if self.connected:
            collection = self.connection["products"]
            collection.update_one({"_id": product_id}, {"$pull": {"watchers": user_id}})
            collection = self.connection["users"]
            collection.update_one({"_id": user_id}, {"$pull": {"watched_products": product_id}})
            return True
        return False
    
    