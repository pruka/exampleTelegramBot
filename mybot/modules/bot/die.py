from pyrogram import filters, Client
from Config import *
from pyrogram.types import Message
from asyncio.exceptions import CancelledError

@Client.on_message(filters.command("die") & filters.user(OWNER_ID))
async def shutdown(bot:Client, msg: Message):
    try:
        await msg.reply("**Öyle ölmem kanka. Füze at **🚀")
        exit(0)
    except Exception as e:
        print(e)
        await msg.reply("**Bir sorun var knk. Öldüremedin beni :D**")

@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def res(bot:Client, msg:Message):
    a = await msg.reply_text("**Restart atılıyor...**")
    await a.edit(f"**Bot yeniden başlatılıyor...**")
    await a.edit(f"**Bot başlatıldı.**")
    try:
        import sys
        from os import environ, execle

        args = [sys.executable, "-m", "mybot"]

        execle(sys.executable, *args, environ)
    except CancelledError:
        print(0)
    except Exception as e:
        print(e)
