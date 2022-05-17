# pylint: disable=super-init-not-called
class MissingPropertiesException(Exception):
    def __init__(self, message="Missing properties in the object"):
        self.message = message
