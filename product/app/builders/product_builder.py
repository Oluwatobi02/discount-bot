from app.product import Product
class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def add_name(self, name):
        self.product.set_name(name)
        return self

    def add_price(self, price):
        self.product.set_price(price)
        return self

    def add_original_price(self, original_price):
        self.product.set_original_price(original_price)
        return self
    def add_currency(self, currency):
        self.product.set_currency(currency)
        return self
    def add_discount(self,discount):
        self.product.set_discount(discount)
        return self
    def add_product_condition(self, product_condition):
        self.product.set_product_condition(product_condition)
        return self
    def add_link(self, link):
        self.product.set_link(link)
        return self
    def add_image(self, image):
        self.product.set_image(image)
        return self
    
    def build(self):
        return self.product