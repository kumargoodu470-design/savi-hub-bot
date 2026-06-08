from pyrogram import Client
from pyrogram.types import CallbackQuery

from handlers.forcejoin import check_force_join

@Client.on_callback_query()
async def verify_callback(client, callback: CallbackQuery):

    if callback.data != "verify_join":
        return

    joined = await check_force_join(
        client,
        callback.from_user.id
    )

    if joined:

        await callback.message.edit_text(
            "✓ Access Verified\n\nWelcome to SAVI HUB"
        )

    else:

        await callback.answer(
            "Please join the channel first.",
            show_alert=True
        )
