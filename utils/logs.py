import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
        handlers=[RotatingFileHandler('./logs/wooadmin.log', maxBytes=10000000, backupCount=10)],
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')