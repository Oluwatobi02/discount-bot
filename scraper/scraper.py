class ScraperFactory:
    @staticmethod
    def get_scraper(scraper):
        if scraper == "amazon":
            return AmazonScraper()
        if scraper == "ebay":
            return EbayScrapper()
        else:
            raise ValueError("Unknown site")


    

class AmazonScraper:

    name = "amazon"

    def scrape(self, url):
        print(f"scraping {self.name}/{url}")


class EbayScrapper:

    name = "ebay"

    def scrape(self, url):
        print(f"scraping {self.name}/{url}")
