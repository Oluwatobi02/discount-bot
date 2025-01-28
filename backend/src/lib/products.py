from state import ApplicationState
from src.factories.product_factory.product_fetcher_factory import ProductFetcherFactory
import requests
import time
app = ApplicationState()
def check_prices():
    while True:
        try:
            products = app.db.get_watched_products()

            for product in products:
                product_fetcher = ProductFetcherFactory.get_product_fetcher('ebay')
                price = product_fetcher.get_product_price(product)
                if price < float(product.price):
                    app.db.update_product_price(product.id, price)
                    requests.get(f"http://localhost:5000/products/{product.id}/notify")
        except Exception as e:
            print(e)
        time.sleep(3600)

                