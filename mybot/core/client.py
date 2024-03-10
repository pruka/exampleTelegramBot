from Config import *
from pyrogram import Client
import asyncio
from pyrogram.types import BotCommand
app = Client(
    name="mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="mybot/modules"),
    in_memory=True
)