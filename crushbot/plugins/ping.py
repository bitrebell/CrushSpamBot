from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from telethon import events
from datetime import datetime

@CrushBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@CrushBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@CrushBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@CrushBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@CrushBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Ping Pong!\n\nCrush Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nPing:- {ms} ms\n\nCrush Spam Bot On Fire")
