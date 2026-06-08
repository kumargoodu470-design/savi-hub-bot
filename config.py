from os import getenv
from dotenv import load_dotenv

load_dotenv()

# ==========================
# SAVI HUB CONFIG
# ==========================

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# MongoDB
MONGO_URI = getenv("MONGO_URI", "")

# Channels
FORCE_CHANNEL = getenv("FORCE_CHANNEL", "")
STORAGE_CHANNEL = int(getenv("STORAGE_CHANNEL", "0"))

# Branding
BOT_NAME = "SAVI HUB"
BOT_OWNER = "SAVI AI"

# Images
WELCOME_IMAGE = "assets/welcome.png"
ERROR_IMAGE = "assets/spelling_error.png"
LOGO_IMAGE = "assets/logo.png"
