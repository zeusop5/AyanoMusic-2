import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zeus.filters import command
from Zeus.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Zeus.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**ʜᴇʏ ɢᴜʏꜱ 
ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.
ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ + ꜱᴘᴀᴍ + ᴠᴄʀᴀɪᴅ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ..
ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ᴍᴀɢɴᴇsɪᴜᴍ xᴅ](t.me/MAGNESIUM_XD)
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 💖ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ😉 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url=f"https://t.me/About_Zeus_xD"
                    ),
                    InlineKeyboardButton(
                        "•ᴏᴡɴᴇʀ•", url="https://t.me/MAGNESIUM_XD"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "♲︎︎︎ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🇮🇳", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bf9f444677e4d565542a6.jpg",
        caption=f"""ᴛʜᴀɴᴋᴅ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ғᴏʀ ᴀɴʏ ǫᴜᴇʀʏ ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/About_Zeus_xD")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/187646e964cd12329f1de.jpg",
        caption=f"""ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ sᴛᴀʀs""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://t.me/About_Zeus_xD")
                ]
            ]
        ),
    )
