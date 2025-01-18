from flask import Flask, jsonify
from app.builders.product_builder import ProductBuilder
from app.factories.product_fetcher_factory import ProductFetcherFactory
from app.db.db import Database
from state import ApplicationState
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

flask_app = Flask(__name__)

app = ApplicationState()
app.set_db(Database())
app.set_app(flask_app)
@app.app.route('/')
def index():
    return "Hello World"

@app.app.route('/product', methods=["POST"])
def create_product():
    try:
        app.db.insert_product(product)
        return "Product created"
    except Exception as e:
        print(e)
        return "Product not created"
@app.app.route('/products', methods=["GET"])
def get_products():
    try:
        products = app.db.get_products()
        return jsonify(products)
    except Exception as e:
        print(e)
        return "Products not found"




app.run()

