from flask import Flask, jsonify, request
from app.factories.product_fetcher_factory import ProductFetcherFactory
from app.db.db import Database
from state import ApplicationState
from app.builders.user_builder import UserBuilder
flask_app = Flask(__name__)

app = ApplicationState()
app.set_db(Database())
app.set_app(flask_app)

@app.app.route('/')
def index():
    app.analytics["/ GET"] = app.analytics.get("/ GET", 0) + 1
    return "Hello World"

@app.app.route('/products', methods=["POST"])
def create_product():
    try:
        app.analytics["/products POST"] = app.analytics.get("/products POST", 0) + 1
        body = request.get_json()
        fetcher = request.args.get("fetcher")
        if fetcher is not None:
            product_fetcher = ProductFetcherFactory.get_product_fetcher(fetcher)
            product = product_fetcher.build_product(body)
            app.db.insert_product(product)
            return "Product created"
        return "Product not created"
    except Exception as e:
        print(e)
        return "Product not created"
    
@app.app.route("/fetch", methods=["GET"])
def fetch():
    app.analytics["/fetch GET"] = app.analytics.get("/fetch GET", 0) + 1
    fetcher = request.args.get("fetcher")
    if fetcher is not None:
        product_fetcher = ProductFetcherFactory.get_product_fetcher(fetcher)
        product_result = product_fetcher.fetch()
        return jsonify(product_result)
    return "fetcher not found or problem with fetcher"

@app.app.route('/products', methods=["GET"])
def get_products():
    app.analytics["/products GET"] = app.analytics.get("/products GET", 0) + 1
    try:
        page = request.args.get("page", 1)
        user_id = request.headers.get("userid")
        print(user_id)
        skip = (int(page) -1) * 10
        products = app.db.get_products(skip)
        products = [product.to_dict(user_id=user_id) for product in products]
        meta = {
            "hasMore": len(products) == 10
        }
        return jsonify({'data': products, 'meta': meta})
    except Exception as e:
        print(e)
        return "Products not found"
    
@app.app.route("/products/<id>/watch")
def watch_product(id):
    user_id = request.headers.get("user")
    if user_id is None:
        return "User not found"
    user = app.db.get_user(user_id)
    app.analytics["/products/<id>/watch GET"] = app.analytics.get("/products/<id>/watch GET", 0) + 1
    product = app.db.get_product(id)
    if product is not None:
        product.add_watcher(user)
        res = app.db.add_watcher_to_product(product.id, user.id)
        return {"message": f"{user.name} is now watching {product.name}", "success": res}
    
@app.app.route("/products/<id>/unwatch")
def unwatch_product(id):
    user_id = request.headers.get("user")
    if user_id is None:
        return "User not found"
    user = app.db.get_user(user_id)
    app.analytics["/products/<id>/unwatch GET"] = app.analytics.get("/products/<id>/unwatch GET", 0) + 1
    product = app.db.get_product(id)
    if product is not None:
        product.add_watcher(user)
        res = app.db.remove_watcher_from_product(product.id, user.id)
        return {"message": f"{user.name} has been removed from watching {product.name}", "success": res}
    
@app.app.route("/sign-up", methods=["POST"])
def sign_up():
    app.analytics["/sign-up POST"] = app.analytics.get("/sign-up POST", 0) + 1
    body = request.get_json()
    res = app.db.insert_user(body)
    if res:
        return {"message": "User created"}
    
@app.app.route("/login", methods=["POST"])
def login():
    app.analytics["/login POST"] = app.analytics.get("/login POST", 0) + 1
    body = request.get_json()
    user = app.db.get_user(body["email"])
    if user is not None and user.password == body["password"]:
        return {"message": "Login successful", "user": user.to_dict()}
    return {"message": "Login failed"}

@app.app.route('/analytics')
def get_analytics():
    app.analytics["/analytics GET"] = app.analytics.get("/analytics GET", 0) + 1
    return jsonify(app.analytics)

@app.app.route('/products/<id>/notify')
def notify_watchers(id):
    app.analytics["/products/<id>/notify GET"] = app.analytics.get("/products/<id>/notify GET", 0) + 1
    product = app.db.get_product(id)
    if product is not None:
        product.notify_watchers("This price has dropped down")
    return {"message": "Notified watchers", "success": True}
app.run()

