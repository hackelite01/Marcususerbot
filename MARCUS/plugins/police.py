
from telethon import events

import asyncio

from uniborg.util import admin_cmd

from userbot import ALIVE_NAME


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Marcus User"

@borg.on(admin_cmd(pattern=r"police"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [
        
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
            "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
            "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",    
            "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
            "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
            "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
            "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
            "**[Marcus Userbot](https://github.com/hackelite01/Marcususerbot) **Police Service Here**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
