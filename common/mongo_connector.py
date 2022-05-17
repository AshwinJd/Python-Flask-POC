import pymongo

from flask import current_app as app
from common import logging_setup

# import logging as logger
logger = logging_setup.get_logger()


def singleton(cls):
    """
    Function ensures there is a single instance of a class being created
    Collects all the object instance id in the variable.
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            logger.info("Creating and returning a new mongo connection")
        else:
            logger.info("Returning existing connection")
        return instances[cls]

    return wrapper


@singleton
class MongoDatabase:
    """
    Added the decorator singleton that will be invoked whenever the class is getting instantiated
    Custom singleton class to generate and open a mongo connection.
    This will help ensure multiple connections are not opened, and forgotten to close later.
    """
    mongo_db = None
    mongo_client = None

    def __init__(self, mongo_url, database_name):
        self.connect(mongo_url, database_name)

    # function to start the mongo connect for a given mongo url and database name
    def connect(self, mongo_url, database_name):
        # If mongo client db obj is already created, return the same instead of creating again.
        if self.mongo_db is not None:
            return self.mongo_db
        self.mongo_client = pymongo.MongoClient(mongo_url)
        my_db = self.mongo_client[database_name]
        # db_list = self.mongo_client.list_database_names()
        # if database_name in db_list:

        self.mongo_db = my_db
        return self.mongo_db

    def get_db_client(self):
        return self.mongo_db

    def close_connection(self):
        return self.mongo_client.close()


# Setup mongo connection and return the mongo db client object
# This will return always the same client object instance. Ensuring only single connection is opened
def mongo_connect(mongo_url, database):
    if not mongo_url:
        app_mongo_url = app.config.MONGO_URL
        app_database = app.config.DATABASE_NAME
    else:
        app_mongo_url = mongo_url
        app_database = database

    db_instnc = MongoDatabase(app_mongo_url, app_database)
    logger.info("Opened Mongo Connection")
    return db_instnc.get_db_client()


def close_connection(mongo_url, database):
    if not mongo_url:
        app_mongo_url = app.config.MONGO_URL
        app_database = app.config.DATABASE_NAME
    else:
        app_mongo_url = mongo_url
        app_database = database
    db_client = MongoDatabase(app_mongo_url, app_database)
    logger.info("Closed Mongo Connection")
    return db_client.close_connection()
