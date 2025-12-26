import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")

ADMINS = [int(i) for i in os.environ.get("ADMINS", "").split(",") if i]

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "REXSaveRestricted")

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))

ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"

KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")
