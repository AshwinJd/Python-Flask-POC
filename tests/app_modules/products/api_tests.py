import json
import unittest
from pathlib import Path

from common import logging_setup
from common import mongo_connector

# Import application object defining the flask setup
from app import application

logger = logging_setup.get_logger()

# Test case
class ProductDAOTests(unittest.TestCase):
    # Setup function is called in the beginning of the testcase
    def setUp(self):
        # Useing test.client() to make API calls to the server
        self.app = application.test_client()

    def test_successful_read_products_api(self):
        database_connect = mongo_connector.mongo_connect(application.config['MONGO_TEST_URL'],
                                                         application.config['DATABASE_TEST'])
        collection = database_connect["products"]

        # Clear the collection before starting the mock insert, so that all previous mocks are deleted, starting with fresh mock
        collection.delete_many({})
        path_directory = Path(__file__).parent.resolve()

        path = str(path_directory) + "/mockdata.json"
        with open(path, ) as mockfile:
            mock = json.load(mockfile)
        product_mock = mock["productMock"]

        collection.delete_many({})

        # Inserting a single record of product to test
        collection.insert_one(product_mock)
        # Testing the insertion was successful or not
        saved_record_count = collection.count_documents({})
        assert saved_record_count == 1

        response = self.app.get('/api/v1/products')
        assert(json.loads(response.text)[0]["productId"]) == product_mock["productId"]


# executing all the test cases
if __name__ == '__main__':
    unittest.main()
