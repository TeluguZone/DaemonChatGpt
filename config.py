import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "24830912"))
API_HASH = environ.get("API_HASH", "a1a1775593531b90850b8b82e3b14940")
BOT_TOKEN = environ.get("BOT_TOKEN", "6798016250:AAGpPgvpXx3O2rLItE-3DcZjzNxOeCLiJOE")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002000741508"))
ADMINS = int(environ.get("ADMINS", "809614790"))
DB_URI = environ.get("DB_URI", "mongodb+srv://Orangepeel:applelayer@cluster0.0wwtjws.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
