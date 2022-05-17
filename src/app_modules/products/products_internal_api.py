from flask import Blueprint, jsonify
from src.app_modules.products import products_controller
from common import logging_setup

products_apis = Blueprint('products_apis', __name__)

logger= logging_setup.get_logger()


@products_apis.route("/products", methods=["GET"])
def get_products():
    logger.debug("Reading all the products")
    data = products_controller.get_products()
    return jsonify(data)
