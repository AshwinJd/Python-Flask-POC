from flask import Blueprint, jsonify
from common import logging_setup

employee_apis = Blueprint('employee_apis', __name__)

logger = logging_setup.get_logger()

@employee_apis.route("/employees")
def get_employees():
    data = {}
    logger.debug("LOGS")
    return jsonify(data)
