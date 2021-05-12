###Check if userbot alive.

### @hackelitebotlist

import asyncio

from telethon import events

from uniborg.util import admin_cmd

from userbot import ALIVE_NAME

from telethon.tl.types import ChannelParticipantsAdmins

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Marcus User"

if Config.SUDO_USERS:

    sudo = "Enabled"

else:

    sudo = "Disabled"

edit_time = 5

""" =======================CONSTANTS====================== """

file1 = "https://telegra.ph/file/5a488103befb5511aa7bd.jpg"

file2 = "https://telegra.ph/file/6a459fc4387a968c9397f.jpg"

file3 = "https://telegra.ph/file/4e96d2e60cbab4876e671.mp4"

""" =======================CONSTANTS====================== """

pm_caption = "**This is Marcus Userbot**\n\n"

pm_caption += "Hi THERE {DEFAULTUSER} MASTER ! I am Alive. All functions are working properly.\n\n"

pm_caption += "饾殏饾殐饾櫚饾殐饾殑饾殏\n"

pm_caption += "岽涐磭薀岽囜礇蕼岽徤� 岽犪磭蕗. : (1.16.04)\n"

pm_caption += "岽樖忈礇蕼岽徤� : (3.8.3)\n"

pm_caption += "岽贯祪食岫溼禈刷 :  **1.0.01** [Ask Support Group Master](t.me/hackelitebotlist)\n"

pm_caption += "岽搬祪岬椺祪岬囜祪刷岬� status : All Fine\n"

pm_caption += f"My Pro Master : {DEFAULTUSER}\n\n"

pm_caption += "Deploy Me Now (https://github.com/hackelite01/Marcususerbot.git)\n\n"

pm_caption +="岽溼礃岽浬磵岽�  :** `{uptime}'\n"

pm_caption += "[MARCUS](https://t.me/hackelitebotlist) For Latest Updates\n\n"

pm_caption += "SYSTEM HEALTH : STABLE "

@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):

    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)

    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)

    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)

    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    

    await asyncio.sleep(edit_time)

    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    

    await asyncio.sleep(edit_time)

    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    

    await asyncio.sleep(edit_time)

    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    
