"""
Made By @TeleBotHelp Keep Credits If You Are Goanna Kang This Lol
And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script
Usage .actressdp I'm Not Responsible For Any Ban caused By This
"""
# (C) @hackelitebotlist
# ANIME DP
# GOT THIS FROM TELEBOT
# KEEP CREDITS IF YOU KANG 
# SLIHTLY EDITED BY @mayank1rajput
# (C) TELEBOT @Xditya
# KEEP ABove Lines 

import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from userbot import CMD_HELP
from userbot.utils import admin_cmd

COLLECTION_STRING = [
    "cute-anime-wallpapers-hd",
    "anime-christmas-wallpaper-hd",
    "anime-samurai-girl-wallpaper",
    "4k-anime-wallpapers",
    "2560-x-1440-wallpaper-anime",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile(r"/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@borg.on(admin_cmd(pattern="setanimedp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Anime DP..\n\nDone !!! Check Your DP in 5 seconds. By [MARCUSUSERBOT](https://github.com/hackelite01/Marcusserbot)**"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600)  # Edit this to your required needs


CMD_HELP.update(
    {"animedp": "➟ `.animedp`\nStart auto-changing anime profile pic for your account."}
)
