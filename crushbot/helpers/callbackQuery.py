from crushbot import *
from crushbot import CrushBot1, CrushBot2, CrushBot3, CrushBot4, CrushBot5
from crushbot.help import *
from crushbot.helpers.commands import *
from telethon import events


@CrushBot1.on(events.CallbackQuery(data=b'alive'))
@CrushBot2.on(events.CallbackQuery(data=b'alive'))
@CrushBot3.on(events.CallbackQuery(data=b'alive'))
@CrushBot4.on(events.CallbackQuery(data=b'alive'))
@CrushBot5.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'ping'))
@CrushBot2.on(events.CallbackQuery(data=b'ping'))
@CrushBot3.on(events.CallbackQuery(data=b'ping'))
@CrushBot4.on(events.CallbackQuery(data=b'ping'))
@CrushBot5.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'raid'))
@CrushBot2.on(events.CallbackQuery(data=b'raid'))
@CrushBot3.on(events.CallbackQuery(data=b'raid'))
@CrushBot4.on(events.CallbackQuery(data=b'raid'))
@CrushBot5.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'replyraid'))
@CrushBot2.on(events.CallbackQuery(data=b'replyraid'))
@CrushBot3.on(events.CallbackQuery(data=b'replyraid'))
@CrushBot4.on(events.CallbackQuery(data=b'replyraid'))
@CrushBot5.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'spam'))
@CrushBot2.on(events.CallbackQuery(data=b'spam'))
@CrushBot3.on(events.CallbackQuery(data=b'spam'))
@CrushBot4.on(events.CallbackQuery(data=b'spam'))
@CrushBot5.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'pspam'))
@CrushBot2.on(events.CallbackQuery(data=b'pspam'))
@CrushBot3.on(events.CallbackQuery(data=b'pspam'))
@CrushBot4.on(events.CallbackQuery(data=b'pspam'))
@CrushBot5.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'extras'))
@CrushBot2.on(events.CallbackQuery(data=b'extras'))
@CrushBot3.on(events.CallbackQuery(data=b'extras'))
@CrushBot4.on(events.CallbackQuery(data=b'extras'))
@CrushBot5.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@CrushBot1.on(events.CallbackQuery(data=b'back'))
@CrushBot2.on(events.CallbackQuery(data=b'back'))
@CrushBot3.on(events.CallbackQuery(data=b'back'))
@CrushBot4.on(events.CallbackQuery(data=b'back'))
@CrushBot5.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 