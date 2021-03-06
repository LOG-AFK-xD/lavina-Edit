from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
     await message.reply_photo("https://telegra.ph/Rishabh-Bhan-12-06")
     await message.reply_text(
        f"""ð **â â° Wá´Êá´á´á´á´...FÊÉªá´É´á´s  {message.from_user.mention()} !**\n
ð â [â°ðºÉªá´Êá´ â ðá´Êá´á´â°](https://t.me/{BOT_USERNAME}) **Há´ÊÊá´...FÊÉªá´É´á´s I Aá´ PÊá´ÊÉªÉ´É¢ Má´sÉªá´ IÉ´ Yá´á´Ê GÊá´á´á´!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âððð ðð ðð ðððððâ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],                
                [
                    InlineKeyboardButton("ðððððððð", callback_data="cbcmds"),
                    InlineKeyboardButton("ð«ððððððððð", url=f"https://t.me/log_afk"),
                ],
                [
                    InlineKeyboardButton(
                        "ðððððððððª", url=f"https://t.me/UNIQUE_SOCIETY"
                    ),
                    InlineKeyboardButton(
                        "ð ððððð ð«", url=f"https://t.me/ALL_DEAR_COMRADE"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ððððððâ¨", url="https://t.me/EVIL_XD_BOY"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )



@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("â¨ ððððð ð«", url=f"https://t.me/UNIQUE_SUPPORT"),
                InlineKeyboardButton(
                    "ðððððððððª", url=f"https://t.me/ALL_DEAR_COMRADE"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\nâ¨ Bot is working normally\nð My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nâ¨ Bot Version: `v{__version__}`\nð Pyrogram Version: `{pyrover}`\nâ¨ Python Version: `{__python_version__}`\nð PyTgCalls version: `{pytover.__version__}`\nâ¨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group's video chat** â¤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("ð `PONG!!`\n" f"â¡ï¸ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "ð¤ bot status:\n"
        f"â¢ **uptime:** `{uptime}`\n"
        f"â¢ **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "â¤ï¸ **ðððððð  ððð ðððððð ðð ð¡ð ð¡ðð ðºððð¢ð !**\n\n"
                "**Promote me as administrator of the Group, otherwise I will not be able to work properly, and don't forget to type /userbotjoin for invite the assistant.**\n\n"
                "**Once done, type** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ðððððððððª", url=f"https://t.me/UNIQUE_SOCIETY"),
                            InlineKeyboardButton("ð ððððð ð«", url=f"https://t.me/ALL_DEAR_COMRADE")
                        ],
                        [
                            InlineKeyboardButton("ð¤ Assistant", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
