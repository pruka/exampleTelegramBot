from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("hello"))
async def hello(bot:Client, message:Message):
    await message.reply("hi!")