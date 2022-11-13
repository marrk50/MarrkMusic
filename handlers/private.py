import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""✰ʜᴇʟʟᴏ... {message.from_user.mention()} , 
ᴍʏ ɴᴀᴍᴇ [{bn}](t.me/{bu}) .
ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ
ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "📨 Channel ", url=f"https://t.me/marrkmusic"
                    ),
                    InlineKeyboardButton(
                        "📨 Support ", url=f"https://t.me/craxymarrk"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/Marrk-85"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://github.com/Marrk-85/MarkMusic"
                    )]
            ]
       ),
    )
