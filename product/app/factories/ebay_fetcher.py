import requests
from app.interfaces.product_fetcher import IProductFetcher

class EbayProductFetcher(IProductFetcher):
    url = "https://ebay-data-scraper.p.rapidapi.com/deals/fashion"
    headers = {
        "x-rapidapi-key": "92e9145017mshb3d01f49ef46cdep163f84jsnfb4065ccd7e3",
        "x-rapidapi-host": "ebay-data-scraper.p.rapidapi.com"
    }

    name = "ebay"

    def scrape(self):
        # response = requests.get(self.url, headers=self.headers)
        print(f"scraping {self.name}/{self.url}")
        # print(response.json())

    def format_product(self):
        pass
