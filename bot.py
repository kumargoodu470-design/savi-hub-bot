from pyrogram import Client
from config import *

app = Client(
    "savihub",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import handlers.start
import handlers.verify

print("SAVI HUB Started")

app.run()
