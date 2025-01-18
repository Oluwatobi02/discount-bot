import requests
import os
from dotenv import load_dotenv
from app.interfaces.product_fetcher import IProductFetcher
load_dotenv()
class EbayProductFetcher(IProductFetcher):
    url = "https://ebay-data-scraper.p.rapidapi.com/deals/fashion"
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY", ""),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST", ""),
    }

    name = "ebay"

    def fetch(self):
        # response = requests.get(self.url, headers=self.headers)
        print(f"scraping {self.name}/{self.url}")
        # print(response.json())

    def format_product(self):
        pass
