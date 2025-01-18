from app.interfaces.product_fetcher import IProductFetcher

class AmazonProductFetcher(IProductFetcher):

    name = "amazon"
    url = "https://www.amazon.com"

    def fetch(self):
        print(f"fetching {self.name}/{self.url}")
    
    def format_product(self):
        pass
