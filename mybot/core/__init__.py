from Config import *
from pyrogram import Client, __version__, idle
import logging
from .client import app
from .sendLogMessages import *
from tglogging import TelegramLogHandler
from logging.handlers import RotatingFileHandler
if LOGGING == "FileLog":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=[
            RotatingFileHandler(
                f"{PROJECT_NAME}.txt", maxBytes=5000000, backupCount=10
            ),
            logging.StreamHandler(),
        ],
    )
    logging.getLogger("pyrogram")
    logging.getLogger(f"{PROJECT_NAME}")