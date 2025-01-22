from src.user import User
class UserBuilder:
    def __init__(self):
        self.user = User()

    def add_name(self, name):
        self.user.set_name(name)
        return self
    def add_email(self, email):
        self.user.set_email(email)
        self.user.set_id(email)
        return self
    def add_phone(self, phone):
        self.user.set_phone(phone)
        return self
    def add_password(self, password):
        self.user.set_password(password)
        return self
    def add_watched_products(self, watched_products):
        self.user.set_watched_products(watched_products)
        return self
    def build(self):
        return self.user
    