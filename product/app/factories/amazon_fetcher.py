from app.interfaces.product_fetcher import IProductFetcher

class AmazonProductFetcher(IProductFetcher):

    name = "amazon"
    url = "https://www.amazon.com"

    def scrape(self):
        print(f"scraping {self.name}/{self.url}")
    
    def format_product(self):
        pass
