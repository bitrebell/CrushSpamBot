from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from telethon import events
from datetime import datetime

PING_PIC = "https://te.legra.ph/file/c037be45ae763bde8c892.jpg"

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
        await e.client.edit_message(message, f" {PING_PIC}\n𝐏𝐈𝐍𝐆 𝐏𝐎𝐍𝐆!!!\n***--------------***\n𝐂𝐑𝐔𝐒𝐇 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓\n***--------------***\n𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n***--------------***\n𝐏𝐈𝐍𝐆!!:- {ms} ms\n***--------------***\n𝐂𝐑𝐔𝐒𝐇 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓 𝐎𝐍 𝐅𝐈𝐑𝐄༗.")
