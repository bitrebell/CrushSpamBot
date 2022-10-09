from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
Crush Spam Bot Is Alive!

My Master:- {master}

Bot Version:- `{BOT_VERSION}`

Telethon Version:- `{version.__version__}`

Moi God:- f"[Aadil](tg://user?id={5106664049})

{BIO_MSG}
"""

@CrushBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@CrushBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@CrushBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@CrushBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@CrushBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
