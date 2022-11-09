from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from telethon import events, Button


data  = [
    Button.url("Channel", url="t.me/crushbot_support"),
    Button.url("Repo", url="https://GitHub.com/Darkranger00/CrushSpamBot"),
    Button.url("Group", url="https://t.me/zgarmy1")
]


@CrushBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@CrushBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@CrushBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@CrushBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@CrushBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Aadil](tg://user?id={5652782615})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},
    This is Crush Spam Bot.
    A Powerfull Spam Bot With a
    large abusive database.
    So,enjoy the Game!!😈😈
***---------------------------------------***
Owner:- {myOwner}
***---------------------------------------***
Sudo:- {sudo_user}
***---------------------------------------***
Creator:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
