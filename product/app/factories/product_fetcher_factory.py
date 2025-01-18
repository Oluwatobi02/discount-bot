from app.factories.amazon_fetcher import AmazonProductFetcher
from app.factories.ebay_fetcher import EbayProductFetcher

class ProductFetcherFactory:
    @staticmethod
    def get_product_fetcher(product_fetcher):
        """
        ONLY TWO TYPES OF FACTORY
        PASS IN "amazon" or "ebay"
        """
        if product_fetcher == "amazon":
            return AmazonProductFetcher()
        if product_fetcher == "ebay":
            return EbayProductFetcher()
        else:
            raise ValueError("Unknown fetcher")
