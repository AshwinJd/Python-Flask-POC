import os

class Config:
    """
    Environment variable can be set to use instead of the default values.
    """
    MONGO_URL = os.getenv("MONGO_URL") or "mongodb://localhost:27017/sampleDB"
    DATABASE_NAME = os.getenv("DATABASE_NAME") or "sampleDB"
    MONGO_TEST_URL = os.getenv("MONGO_URL") or "mongodb://localhost:27017/sampleDB"
    DATABASE_TEST = os.getenv("DATABASE_NAME") or "sampleDB"
    SECRET = os.getenv("SECRET") or "lksjcl390s-0dfdfsmc2"
    ACCESS_ROLES_MAPPING = {
        # Keeping a standard format, <modulename>:<access grant>
        "SUPERVISOR": ["EMPLOYEE:READ_ALL", "EMPLOYEE:READ", "EMPLOYEE:CREATE", "PRODUCT:CREATE", "PRODUCT:READ"],
        "MEMBER": ["EMPLOYEE:READ", "PRODUCT:READ", "EMPLOYEE:CREATE"],
    }
