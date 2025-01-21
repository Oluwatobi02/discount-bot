# i want this to have context of my application
import os
import threading
from dotenv import load_dotenv
from flask_cors import CORS
from app.db.db import Database
load_dotenv()
class ApplicationState:
    __instance = None
    state = None
    db = None
    app = None
    analytics = {}

    __lock = threading.Lock()
    
    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(ApplicationState, cls).__new__(cls)
                cls.__instance.state = None
        return cls.__instance

    def set_state(self, state):
        self.state = state
    def get_state(self):
        return self.state

    def reset_state(self):
        self.state = None
        self.db = None
        self.app = None

    def set_db(self, db : Database):
        self.db = db

    def get_db(self):
        return self.db
    
    def set_app(self, app):
        if self.app is None:
            self.app = app
    def get_app(self):
        return self.app
    
    def register_route(self, route, view_func):
        if self.app is not None:
            self.app.route(route)(view_func)
        return self
    
    def initialize(self):
        if self.state is None:
            self.db = self.db.connect()
            # CORS(self.app)
            self.db.create_collections()
            self.set_state("running")
            # return self.app.run(port=5000, host="0.0.0.0")
        print("Error running app")
        return "nothing"
    
    