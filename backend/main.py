from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from src.factories.product_factory.product_fetcher_factory import ProductFetcherFactory
from src.lib.products import check_prices
import threading
from src.db.db import Database
from state import ApplicationState
import random

flask_app = Flask(__name__)
CORS(flask_app)

app = ApplicationState()
app.set_db(Database())
app.set_app(flask_app)

@app.app.route('/')
def index():
    app.analytics["/ GET"] = app.analytics.get("/ GET", 0) + 1
    return "Hello World"

@app.app.route('/checkprices')
def check_prices_route():
    app.analytics["/checkprices GET"] = app.analytics.get("/checkprices GET", 0) + 1
    t1 = threading.Thread(target=check_prices)
    t1.start()
    
    return "Checking prices"
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
        skip = (int(page) -1) * 10
        products = app.db.get_products(skip)
        products = [product.to_dict(user_id=user_id) for product in products]
        random.shuffle(products)
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
    user_activity = {
        "user": user_id,
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
        "action": "watch",
        "timestamp": datetime.now().isoformat(),
        "metadata": {
            "product": product.id,
            "product_name": product.name
        },
        "device": request.headers["User-Agent"]

    }
    if product is not None:
        product.add_watcher(user)
        res = app.db.add_watcher_to_product(product.id, user.id)
        try:
            app.db.insert_user_activity(user_activity)
        except:
            pass
        return {"message": f"{user.name} is now watching {product.name}", "success": res}
    
@app.app.route("/products/<id>/unwatch")
def unwatch_product(id):
    user_id = request.headers.get("user")
    if user_id is None:
        return "User not found"
    user = app.db.get_user(user_id)
    app.analytics["/products/<id>/unwatch GET"] = app.analytics.get("/products/<id>/unwatch GET", 0) + 1
    product = app.db.get_product(id)
    user_activity = {
    "user": user_id,
    "ip": request.headers.get('X-Forwarded-For', request.remote_addr),
    "action": "unwatch",
    "timestamp": datetime.now().isoformat(),
    "metadata": {
        "product": product.id,
        "product_name": product.name
    },
    "device": request.headers["User-Agent"]
}
    if product is not None:
        product.add_watcher(user)
        res = app.db.remove_watcher_from_product(product.id, user.id)
        try:
            app.db.insert_user_activity(user_activity)
        except:
            pass
        return {"message": f"{user.name} has been removed from watching {product.name}", "success": res}
    
@app.app.route("/sign-up", methods=["POST"])
def sign_up():
    app.analytics["/sign-up POST"] = app.analytics.get("/sign-up POST", 0) + 1
    body = request.get_json()
    res = app.db.insert_user(body)
    if res:
        user_activity = {
            "user": body["email"],
            "ip": request.headers.get('X-Forwarded-For', ''),
            "action": "sign-up",
            "timestamp": datetime.now().isoformat(),
            "metadata": {},
            "device": request.headers["User-Agent"]
        }
        try:
            app.db.insert_user_activity(user_activity)
        except:
            pass
        return {"message": "User created"}
    
@app.app.route("/login", methods=["POST"])
def login():
    app.analytics["/login POST"] = app.analytics.get("/login POST", 0) + 1
    body = request.get_json()
    user = app.db.get_user(body["email"])
    user_activity = {
    "user": user.id,
    "ip": request.headers.get('X-Forwarded-For', ''),
    "action": "login",
    "timestamp": datetime.now().isoformat(),
    "metadata": {},
    "device": request.headers["User-Agent"]
}
    
    if user is not None and user.password == body["password"]:
        try:
            app.db.insert_user_activity(user_activity)
        except:
            pass
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
        product.notify_watchers()
        return {"message": "Notified watchers", "success": True}
    return {"message": "Product not found", "success": False}



from src.factories.notification_factory.sms import SMSClient
sms_client = SMSClient()

@app.app.route('/contacts/list/', methods=["POST"])
def add_new_contact():
    res = sms_client.create_new_list('dealspree')
    return jsonify({'data': res})  


app.initialize()
# flask_app.run(port=5000, host="0.0.0.0")


