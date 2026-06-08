from pyrogram import filters
from pyrogram.types import ForceReply

from bot import app
from database.mongo import add_file

pending_uploads = {}

ADMIN_ID = 6024953191


@app.on_message(filters.video & filters.user(ADMIN_ID))
async def receive_video(client, message):

    pending_uploads[message.from_user.id] = message.video.file_id

    await message.reply_text(
        "Movie Name | Quality | Size\n\nExample:\nAnimal | 1080p | 2.8 GB",
        reply_markup=ForceReply(True)
    )


@app.on_message(filters.reply & filters.user(ADMIN_ID))
async def save_movie(client, message):

    if message.from_user.id not in pending_uploads:
        return

    try:

        title, quality, size = [
            x.strip()
            for x in message.text.split("|")
        ]

        file_id = pending_uploads[
            message.from_user.id
        ]

        await add_file(
            title,
            quality,
            size,
            file_id
        )

        del pending_uploads[
            message.from_user.id
        ]

        await message.reply_text(
            f"Saved Successfully\n\n{title}\n{quality}\n{size}"
        )

    except:

        await message.reply_text(
            "Wrong format.\n\nUse:\nMovie Name | Quality | Size"
        )
