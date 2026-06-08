from pyrogram import filters
from pyrogram.types import ForceReply

from bot import app

pending_uploads = {}


ADMIN_ID = 6024953191  

@app.on_message(filters.video & filters.user(ADMIN_ID))
async def receive_video(client, message):

    pending_uploads[message.from_user.id] = message.video.file_id

    await message.reply_text(
        "Reply format:\n\nMovie Name | Quality | Size\n\nExample:\nAnimal | 1080p | 2.8 GB",
        reply_markup=ForceReply(True)
    )
