from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import app
from database.mongo import get_files


@app.on_message(filters.text & ~filters.command(["start"]))
async def search_file(client, message):

    query = message.text.strip()

    files = await get_files(query)

    if not files:

        await message.reply_text(
            "No files found."
        )

        return

    buttons = []

    for file in files:

        buttons.append(
            [
                InlineKeyboardButton(
                    f"{file['quality']} • {file['size']}",
                    callback_data=f"file_{str(file['_id'])}"
                )
            ]
        )

    await message.reply_text(
        f"Results for: {query}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
