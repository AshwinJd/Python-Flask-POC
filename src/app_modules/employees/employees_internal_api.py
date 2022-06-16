import json

from bson import json_util
from flask import Blueprint, request

from common import logging_setup
from src.app_modules.authentication.authentication_middlerware import auth_middleware
from src.app_modules.employees import employees_controller

employee_apis = Blueprint('employee_apis', __name__)

logger = logging_setup.get_logger()


@employee_apis.route("/employees")
@auth_middleware(required_grants=["EMPLOYEE:READ_ALL"])
def get_employees(userlogged):
    logger.debug("userlogged %s", userlogged)
    response = employees_controller.get_employees()
    return json.loads(json_util.dumps(response)), response["status"]


@employee_apis.route("/employees", methods=["POST"])
@auth_middleware(required_grants=["EMPLOYEE:CREATE"])
def post_employees(current_user):
    try:
        employee = request.get_json()
        employee["createdBy"] = current_user["username"]
        response = employees_controller.save_employees(employee)
        return json.loads(json_util.dumps(response)), response["status"]

    except Exception as exc:
        logger.error("In API layer, Exception occurred while saving a new employee record - %s", exc)
        response = {
            "status": 400,
            "result": {},
            "error": {
                "message": "Unable to save record"
            }
        }
        return json.loads(json_util.dumps(response)), response["status"]
