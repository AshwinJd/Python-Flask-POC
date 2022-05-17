import logging
from logging import config

log_config = {
    "version": 1,
    "root": {
        "handlers": ["console"],
        "level": "DEBUG"
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters": {
        "std_out": {
            "format": '%(asctime)s %(levelname)-8s %(message)s',
            "datefmt": "%d-%m-%Y %H:%M:%S"
        }
    },
}

# Disabling the loggers that external to application
# for logger in logging.Logger.manager.loggerDict:
#     logging.getLogger(logger).disabled = True

config.dictConfig(log_config)


def get_logger():
    return logging
