from src.factories.notification_factory.notification_factory import NotificationFactory
class User:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.phone = None
        self.password = None
        self.watched_products = None
    def __str__(self):
        return f"User(name={self.name}, email={self.email}, phone={self.phone}, password={self.password}, watched_products={self.watched_products})"
    def __repr__(self):
        return self.__str__()
    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "watched_products": self.watched_products,
        }
    def set_id(self, id):
        self.id = id
    def add_watched_product(self, product):
        self.watched_products.append(product)
    
    def set_name(self, name):
        self.name = name
    def set_email(self, email):
        self.email = email
    def set_phone(self, phone):
        self.phone = phone
    def set_password(self, password):
        self.password = password
    def set_watched_products(self, watched_products):
        self.watched_products = watched_products
    def notify(self, message):
        notification_client = NotificationFactory.get_notification_client("sms")
        notification_client.send_message(f"+1{self.phone}", message)
        print(f"User {self.name} received message: {message}")