from config import (API_ID, API_HASH, BOT_TOKEN)

from pyrogram import Client

app = Client(
    "MarrkMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

