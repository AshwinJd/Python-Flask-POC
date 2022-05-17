from flask import Flask

from configurations.config import Config
from src.app_modules.products import products_internal_api
from src.app_modules.employees import employees_internal_api

application = Flask(__name__)

# Loading the config to be used to the application
application.config.from_object(Config)

# Registing the API endpoints to the main application, at specific url mount paths
application.register_blueprint(products_internal_api.products_apis, url_prefix="/api/v1")
application.register_blueprint(employees_internal_api.employee_apis, url_prefix="/api/v1")


if __name__ == "__main__":
    application.run(host='0.0.0.0')



