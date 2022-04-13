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
        caption=f"""**✨𝐇ᴇʏ 𝐓ʜᴇʀᴇ 𝐌ʏ 𝐍ᴀᴍᴇ 𝐈s 🌈𝐀ʏᴀɴᴏ 𝐑ᴏʙᴏᴛ🌈 𝐈'ᴍ 𝐀  𝐏ᴏᴡᴇʀғᴜʟʟ 𝐕𝐂 𝐀ɴᴅ  𝐆ʀᴏᴜᴘ 𝐌ᴀɴᴀɢᴇʀ 𝐁ᴏᴛ 𝐖ɪᴛʜ 𝐂ᴏᴏʟ 𝐌ᴏᴅᴜʟᴇs. 𝐅ᴇʟʟ 𝐅ʀᴇᴇ 𝐓ᴏ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘs 𝐇ɪᴛ 𝐇ᴇʟᴘ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐊ɴᴏᴡ 𝐌ʏ 𝐂ᴏᴍᴍᴀɴᴅs✨

┏━━━━━━━━━━━━━━━━━━━━━❥
┣ 𝐔ᴘᴅᴀᴛᴇꜱ -> @MARcos_ZEUS_XD
┣ 𝐒ᴜᴘᴘᴏʀᴛ -> @TheMKHackerX131
┗━━━━━━━━━━━━━━━━━━━━━❥
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/zeusop5/AyanoMusic-2"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/eb9a9acde7a4a3e051556.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/eb9a9acde7a4a3e051556.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/zeusop5/AyanoMusic-2")
                ]
            ]
        ),
    )
