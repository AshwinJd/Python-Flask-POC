import json

from flask import current_app as app

from common import logging_setup
from common import mongo_connector

logger = logging_setup.get_logger()


def save_employees(employee_obj):
    database_connect = mongo_connector.mongo_connect(app.config["MONGO_URL"], app.config["DATABASE_NAME"])
    collection = database_connect['employees']

    inserted_record = collection.insert_one(employee_obj)
    result_record = collection.find_one({"_id": inserted_record.inserted_id}, {'_id': False})

    if result_record is None:
        raise Exception(" unable to new save employee record")

    logger.debug("In Dao layer, new employee record saved successfully")
    return json.loads(json.dumps(result_record))


def get_employee_byid(employee_id):
    database_connect = mongo_connector.mongo_connect(app.config["MONGO_URL"], app.config["DATABASE_NAME"])
    collection = database_connect['employees']

    emp_record = collection.find_one({"empid": employee_id}, {'_id': False})
    logger.info("In Dao layer, successfully returned employee record by Id")

    return json.loads(json.dumps(emp_record))


def get_employees():
    database_connect = mongo_connector.mongo_connect(app.config["MONGO_URL"], app.config["DATABASE_NAME"])
    collection = database_connect['employees']

    emp_record = collection.find({}, {'_id': False})
    logger.info("In Dao layer, successfully returned employees records")

    return json.loads(json.dumps(list(emp_record)))
