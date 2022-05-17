import json
import unittest
from pathlib import Path

from common import logging_setup
from common import mongo_connector

from src.app_modules.products import products_dao
logger = logging_setup.get_logger()
from app import application

# Test case
class ProductDAOTests(unittest.TestCase):
     def test_successful_read_products(self):
        database_connect = mongo_connector.mongo_connect(application.config['MONGO_TEST_URL'],  application.config['DATABASE_TEST'])
        collection = database_connect["products"]

        # Clear the collection before starting the mock insert, so that all previous mocks are deleted, starting with fresh mock
        collection.delete_many({})
        path_directory = Path(__file__).parent.resolve()

        path = str(path_directory) + "/mockdata.json"
        with open(path, ) as mockfile:
            mock = json.load(mockfile)
        product_mock = mock["productMock"]

        # Inserting a single record of product to test
        collection.insert_one(product_mock)

        saved_record_count = collection.count_documents({})
        assert saved_record_count == 1

        # If you want to test code which uses an application context (current_app, g, url_for), push an app_context.
        with application.app_context():
            result_obj = products_dao.get_products()
            assert result_obj[0]["productId"] == product_mock["productId"]
            assert len(result_obj) == 1


# executing all the test cases
if __name__ == '__main__':
    unittest.main()
