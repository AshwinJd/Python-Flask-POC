from flask import Flask, request
from datetime import datetime
from configurations.config import Config
from src.app_modules.products import products_internal_api
from src.app_modules.employees import employees_internal_api
from common import logging_setup
import traceback


logger = logging_setup.get_logger()

application = Flask(__name__)

# Loading the config to be used to the application
application.config.from_object(Config)

# Registing the API endpoints to the main application, at specific url mount paths
application.register_blueprint(products_internal_api.products_apis, url_prefix="/api/v1")
application.register_blueprint(employees_internal_api.employee_apis, url_prefix="/api/v1")

@application.after_request
def after_request(response):
    timestamp = datetime.now().strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response


@application.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = datetime.now().strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s 500 INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
    response = {
        "message": "Internal server error!. Developer at work please try later."
    }
    return response, 400

if __name__ == "__main__":
    application.run(host='0.0.0.0')



