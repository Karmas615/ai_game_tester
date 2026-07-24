import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "game_tester.log",
    maxBytes=500000,
    backupCount=5
)

logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(msg):
    logging.info(msg)
