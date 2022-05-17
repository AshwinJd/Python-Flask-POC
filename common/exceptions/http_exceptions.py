# pylint: disable=super-init-not-called
class BadRequestException(Exception):
    def __init__(self, message="API failed with Bad request"):
        self.message = message


class APIServerException(Exception):
    def __init__(self, message="API failed with internal server exception"):
        self.message = message
