from .client import app
from pythonansi import colors
import sys
from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Config import *

color = colors()

async def sendLogGroupStartMessage():
    #   print(SUDOS)
    uname = app.me
    text = f"""
**@{uname.username} Başarıyla başlatıldı!**

**🖥️ Sürümler:**
__Python Sürümü:__ `{sys.version.split()[0]}`
__Pyrogram Sürümü:__ `{__version__}`

**ℹ️ Bilgiler:**
__Bot ID:__ `{uname.id}`
__Bot Adı:__ `{uname.first_name}`
__Bot Kullanıcı Adı:__ @{uname.username}


__👑By @halillb__
"""
    await app.send_message(
        OWNER_ID,
        text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Destek Grubu", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                ],
            ],
        ),
    )
    color.print(
        f"Log Grubuna [{LOG_CHANNEL}] başlatılma mesajı gönderildi.", color.cyan
    )
    a = f"""
\033[32m Bot Started Successfully\033[0m

\033[33m Bot Name: \033[0m {uname.first_name}\033[0m
\033[33m Bot ID: \033[0m {uname.id}\033[0m
\033[33m Bot Username: \033[0m @{uname.username}\033[0m

\033[33m Pyrogram Version: \033[0m {__version__}\033[0m
\033[33m Python Version: \033[0m {sys.version.split()[0]}\033[0m

\033[33m Log Channel: \033[0m {LOG_CHANNEL}\033[0m
\033[33m By @ - @\033[0m

\033[33m Bot Started At: \033[0m
"""
    print(a)  # Bilgileri ekrana basar.