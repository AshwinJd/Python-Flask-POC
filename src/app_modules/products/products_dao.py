from flask import current_app as app
from common import mongo_connector


def get_products():
    database_connect = mongo_connector.mongo_connect(app.config["MONGO_URL"], app.config["DATABASE_NAME"])
    collection = database_connect['products']

    products_list = collection.find({}, {"_id": 0})

    return list(products_list)
