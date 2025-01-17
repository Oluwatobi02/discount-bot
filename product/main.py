from app.builders.product_builder import ProductBuilder
from app.factories.product_fetcher_factory import ProductFetcherFactory

product_fetcher = ProductFetcherFactory.get_product_fetcher("amazon")

product = ProductBuilder()\
                            .add_name("Air Jordans")\
                            .add_price(10)\
                            .add_original_price(20)\
                            .add_currency("USD")\
                            .add_discount(0.5)\
                            .add_product_condition("new")\
                            .add_link("link")\
                            .add_image("image")\
                            .build()