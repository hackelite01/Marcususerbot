"""
Made By @mayank1rajput Inspired by Xditya Telebot Anime dp 
kang = keep all lines 
dont kang blindly 
after reading this and you removed = U will be blitch son 

# (C) @hackelitebotlist
# Space DP
# GOT THIS Idea FROM TELEBOT
# KEEP CREDITS IF YOU KANG 
# Wrote BY @mayank1rajput
# KEEP ABove Lines 
"""
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
                  "tron-background"
		  "iron-man-jarvis-animated-wallpaper"
		  "batcomputer-wallpaper"
]
# ----------------For @hackelitebotlist-------------------------------------------------------------------Wrote BY @mayank1rajput-----------------------------------------

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

# ----------------For @hackelitebotlist-------------------------------------------------------------------Wrote BY @mayank1rajput-----------------------------------------
@borg.on(admin_cmd(pattern="sethackerdp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting  DP..\n\nDone !!! Check Your DP in 5 seconds. By [MARCUSUSERBOT](https://github.com/hackelite01/Marcususerbot)**"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600)  # Edit this to your required needs

# ----------------For @hackelitebotlist-------------------------------------------------------------------Wrote BY @mayank1rajput-----------------------------------------
