import asyncio
import logging
from telethon import TelegramClient
from crushbot.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "CrushSpamBot"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "crushbot_Support"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://te.legra.ph/file/afa6e09c555316c8dfeb1.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "𝗖𝗥𝗨𝗦𝗛 𝗦𝗣𝗔𝗠𝗕𝗢𝗧 𝗛𝗔𝗩𝗘 𝗔 𝗙𝗨𝗖𝗞𝗜𝗡𝗚 𝗔𝗕𝗜𝗟𝗜𝗧𝗬 𝗧𝗢 𝗙𝗨𝗖𝗞 𝗔𝗟𝗟 𝗢𝗙 𝗬𝗢𝗨༗.!!"


BOT_VERSION = 1.0

GOD_USERS = [5106664049]
DEV_USERS = [5106664049]
MY_USERS = [5106664049]
LIMIT = [5106664049]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global CrushBot1
    global CrushBot2
    global CrushBot3
    global CrushBot4
    global CrushBot5

    if BOT_TOKEN1:
        print("Working On Bot Token 1!")
        try:
            CrushBot1 = TelegramClient("CrushSpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK!")
            await CrushBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "CrushSpamBot1"
            CrushBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await CrushBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2!")
        try:
            CrushBot2 = TelegramClient("CrushSpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!")
            await CrushBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "CrushSpamBot2"
            CrushBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await CrushBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            pass
    
    if BOT_TOKEN3:
        print("Working On Bot Token 3!")
        try:
            CrushBot3 = TelegramClient("CrushSpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK!")
            await CrushBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "CrushSpamBot3"
            CrushBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await CrushBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4!")
        try:
            CrushBot4 = TelegramClient("CrushSpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK!")
            await CrushBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "CrushSpamBot4"
            CrushBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await CrushBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5!")
        try:
            CrushBot5 = TelegramClient("CrushSpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK!")
            await CrushBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "CrushSpamBot5"
            CrushBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await CrushBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())