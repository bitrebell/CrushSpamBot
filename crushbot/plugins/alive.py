from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
𝒚𝒐𝒖 𝒂𝒍𝒔𝒐 𝒘𝒂𝒏𝒕 𝒕𝒉𝒓𝒊𝒍𝒍𝒍𝒆𝒓 𝒋𝒖𝒔𝒕 𝒂𝒘𝒂𝒌𝒆 𝒎𝒆!!
𝒃𝒚 𝒕𝒉𝒆 𝒘𝒂𝒚 𝒄𝒓𝒖𝒔𝒉 𝒔𝒑𝒂𝒎 𝒃𝒐𝒕 𝒊𝒔 𝒂𝒍𝒊𝒗𝒆!!
***-------------------------------***
𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓:- {master}
***-------------------------------***
𝒃𝒐𝒕 𝒗𝒆𝒓𝒔𝒊𝒐𝒏:- `{BOT_VERSION}`
***-------------------------------***
𝒕𝒆𝒍𝒆𝒕𝒉𝒐𝒏 𝒗𝒆𝒓𝒔𝒊𝒐𝒏:- `{version.__version__}`
***-------------------------------***
𝒎𝒐𝒊 𝒈𝒐𝒅༗:- f"[Aadil](tg://user?id={5106664049})
***-------------------------------***
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
