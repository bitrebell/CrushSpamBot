from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from crushbot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Pspam", b'pspam')
], [
    Button.inline("Extras", b'extras')
], [
    Button.url("Channel", "t.me/crushbot_support"),
    Button.url("Group", "t.me/crushbot_support")
]

BACK = [
    Button.inline("Back", b'back')
]

@CrushBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@CrushBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@CrushBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@CrushBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@CrushBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        

