from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from crushbot.helpers.commands import *
from telethon import events, Button

DISPLAY_PICS = "https://te.legra.ph/file/34e099ab7e10d6b65aa04.jpg"

Buttons = [
    Button.inline("𝗔𝗟𝗜𝗩𝗘", b'alive'),
    Button.inline("𝗣𝗜𝗡𝗚", b'ping')
], [
    Button.inline("𝗥𝗔𝗜𝗗", b'raid'),
    Button.inline("𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗", b'replyraid')
], [
    Button.inline("𝗦𝗣𝗔𝗠", b'spam'),
    Button.inline("𝗣𝗦𝗣𝗔𝗠", b'pspam')
], [
    Button.inline("𝐄𝐗𝐓𝐑𝐀𝐒", b'extras')
], [
    Button.url("𝐂𝐇𝐀𝐍𝐍𝐄𝐋", "t.me/crushbot_support"),
    Button.url("𝐆𝐑𝐎 𝐔𝐏", "t.me/zgarmy1")
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
        message = await e.client.send_file(e.chat_id, DISPLAY_PICS, caption="𝐇𝐄𝐘!! 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐂𝐑𝐔𝐒𝐇𝐒 𝐒𝐏𝐀𝐌𝐁𝐎𝐓. 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐘𝐎 𝐔𝐑 𝐇𝐄𝐋𝐏 𝐂𝐎𝐌𝐌𝐀𝐍𝐃!!!", buttons=Buttons)

        

