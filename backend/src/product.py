
class Product():
    def __init__(self):
        self.id = None
        self.name = None
        self.price = None
        self.original_price = None
        self.currency = None
        self.discount = None
        self.product_condition = None
        self.link = None
        self.image = None
        self.watchers = []

        
    def set_name(self, name):
        self.name = name
        
    def set_price(self, price):
        self.price = price
        
    def set_original_price(self, original_price):
        self.original_price = original_price
        
    def set_currency(self, currency):
        self.currency = currency
        
    def set_discount(self, discount):
        self.discount = discount
        
    def set_product_condition(self, product_condition):
        self.product_condition = product_condition
        
    def set_link(self, link):
        self.link = link
        
    def set_image(self, image):
        self.image = image

    def add_watcher(self, watcher):
        self.watchers.append(watcher)
        

    def notify_watchers(self):
        noti_message = f"Product {self.name} ('{self.id}') has a price drop"
        for watcher in self.watchers:
            watcher.notify(noti_message)
    def set_id(self, id):
        self.id = id
        
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, original_price={self.original_price}, currency={self.currency}, discount={self.discount}, product_condition={self.product_condition}, link={self.link}, image={self.image})"
    def __repr__(self):
        return self.__str__()
    def to_dict(self,**kwargs):
        user_id = kwargs.get("user_id", None)
        return {
            "_id": self.id,
            "name": self.name,
            "price": self.price,
            "original_price": self.original_price,
            "currency": self.currency,
            "discount": self.discount,
            "product_condition": self.product_condition,
            "link": self.link,
            "image": self.image,
            "watchers": [watcher.id for watcher in self.watchers],
            "is_watching": any([user_id == users.id for users in self.watchers])
        }