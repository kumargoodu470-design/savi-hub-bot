from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from bot import app

from config import FORCE_CHANNEL
from handlers.forcejoin import check_force_join


@app.on_message(filters.command("start"))
async def start_command(client, message):

    joined = await check_force_join(
        client,
        message.from_user.id
    )

    if not joined:

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Join Channel",
                        url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Verify Access",
                        callback_data="verify_join"
                    )
                ]
            ]
        )

        await message.reply_text(
            "Welcome to SAVI HUB\n\nPlease join our official channel to continue.",
            reply_markup=buttons
        )

        return

    await message.reply_text(
        "Access Granted\n\nWelcome to SAVI HUB."
    )
