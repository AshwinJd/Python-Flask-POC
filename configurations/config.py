import os

class Config:
    """
    Environment variable can be set to use instead of the default values.
    """
    MONGO_URL = os.getenv("MONGO_URL") or "mongodb://localhost:27017/sampleDB"
    DATABASE_NAME = os.getenv("DATABASE_NAME") or "sampleDB"
    MONGO_TEST_URL = os.getenv("MONGO_URL") or "mongodb://localhost:27017/sampleDB"
    DATABASE_TEST = os.getenv("DATABASE_NAME") or "sampleDB"
