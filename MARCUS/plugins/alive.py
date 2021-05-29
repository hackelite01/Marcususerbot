###Check if userbot alive.
### @MarcusUserbot

import asyncio
from telethon import events
from uniborg.util import admin_cmd
from MARCUS import ALIVE_NAME
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

pm_caption += "Hi THERE {ALIVE_NAME} MASTER ! I am Alive. All functions are working properly.\n\n"
pm_caption += "𝙼𝙰𝚁𝙲𝚄𝚂 𝚂𝚃𝙰𝚃𝚄𝚂\n"
pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 : (1.16.04)\n"
pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 : (3.8.3)\n"
pm_caption += "𝙰.𝙸. 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :  **1.0.01**\n"
pm_caption += "𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝚂𝚃𝙰𝚃𝚄𝚂 : All Fine\n"
pm_caption += f"My Pro Master : {ALIVE_NAME}\n\n"
pm_caption += "[Deploy Me Now](https://github.com/hackelite01/Marcususerbot)\n\n"
pm_caption +="𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}'\n"
pm_caption += "[MARCUS](https://t.me/MarcusUserbot) For Latest Updates\n\n"
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
    