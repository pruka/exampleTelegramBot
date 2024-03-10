from .core import *
import asyncio

async def start():
    try:
        await app.start()
        await sendLogGroupStartMessage()
#        await app.send_message(OWNER_ID, "calistim")
        await idle()
    except KeyboardInterrupt:
        print("Keyboardinterrupt error")
        
asyncio.run(start())