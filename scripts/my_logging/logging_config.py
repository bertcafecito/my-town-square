import logging.config
import os
from .logging_filters import SensitiveDataFilter

# Get the directory where this config file is located
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "calendar_data", "logs")

# Ensure logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "sensitive_data_filter": {
            "()": SensitiveDataFilter,
        }
    },
    "formatters": {
        "json": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            "class": "pythonjsonlogger.json.JsonFormatter",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "json",
            "filters": ["sensitive_data_filter"],
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGS_DIR, "app.log"),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
            "formatter": "json",
            "filters": ["sensitive_data_filter"],
        },
    },
    "loggers": {"": {"handlers": ["stdout"], "level": "DEBUG"}},
}


logging.config.dictConfig(LOGGING)
