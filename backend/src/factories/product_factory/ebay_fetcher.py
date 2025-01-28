import requests
import os
from dotenv import load_dotenv
from src.interfaces.product_fetcher import IProductFetcher
from src.builders.product_builder import ProductBuilder
load_dotenv()

class EbayProductFetcher(IProductFetcher):
    url = "https://ebay-data-scraper.p.rapidapi.com/deals/fashion"
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY", ""),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST", ""),
    }

    name = "ebay"

    def fetch(self):
        response = requests.get(self.url, headers=self.headers)
        print(f"scraping {self.name}/{self.url}")
        body = response.json()
        for product in body:

            requests.post("http://localhost:5000/products", json=product, params={"fetcher": self.name})
        return body
    def format_product(self, product):
        return {
            "_id": self.get_id_from_link(product["link"]),
            "name": product["product_name"],
            "link": product["link"],
            "condition": product["product_condition"],
            "price": product["price"],
            "discount": product["discount"],
            "original_price": product["original_price"],
            "currency": product["currency"],
            "image": product["image"]
        }
    
    def get_id_from_link(self, link):
        return link.split('/')[4].split('?')[0]
    def build_product(self, product):
        product = self.format_product(product)
        item = ProductBuilder()\
                            .add_id(product["_id"])\
                            .add_name(product["name"])\
                            .add_price(product["price"])\
                            .add_original_price(product["original_price"])\
                            .add_currency(product["currency"])\
                            .add_discount(product["discount"])\
                            .add_product_condition(product["condition"])\
                            .add_link(product["link"])\
                            .add_image(product["image"])\
                            .build()
        return item

    def get_product_price(self, product):
        res = requests.get(f"https://ebay-data-scraper.p.rapidapi.com/products/{product.id}", headers=self.headers)
        data = res.json()[0]
        return float(data['price'][5:])