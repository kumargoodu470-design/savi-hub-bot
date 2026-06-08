from pyrogram import filters
from bot import app


@app.on_message(filters.document)
async def save_file(client, message):

    await message.reply_text(
        "File received.\n\nSAVI HUB storage system coming soon."
    )
