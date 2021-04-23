# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
#

""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from cowpy import cow

from userbot import CMD_HELP,YOUTUBE_API_KEY
from userbot.utils import register,admin_cmd

# ================= CONSTANT =================
RENDISTR = [
    "`I Know Uh ez Rendi Bhay Dont show Your Randi Pesa Here`",
    "`Jag Suna suna laage Sab #maderchod bhay`",
    "`you talking behind meh wew uh iz my fan now bhay`",
    "`Wanna pass in Life Goto BRAZZER.CAM BHAY`",
    "`Uh iz Pro i iz noob your boob is landi uh are Randi`",
    "`Sellers Nasa calling Uh bhayðŸ˜†`",
    "`Badwoo ki yojna behan bna ke ch*da uh iz badwa its your yozja?`",
    "`CHAND PE CHADA HAI CHANDYAAN KA GHODA TERA NAAM HAI MANSUR TU HAI BEHAN KA LOD*ðŸ˜‚`",
    "`Jab se dil lga baithe tanhai me maa chu*da baithe wo kho gyi kisi aur ke pyar hum apne hi jaato me aag lga baithe`",
    "`Chadii ke ander se lal pani kha se ata hai ky teri masuka ka bhosda bhi paan khata haiðŸ˜‚`",
    "`Sun bhosdi ke By anonyCrew MOHABBAT KE SIWA AUR BHI GAM HAI JAMANE ME BSDK GAND PAHAT JATI HAI PAISA KAMANE ME`",
    "`Thaan liya tha Sayri nhi krege Unka pichwada dekha Alfaaz nikal gye`",
    "`Ravivaar ko dekha Chand Ka Tukra Itna Baar Dekha par Jaath na Ukra`",
    "`Katal kro Tir se Talwar me Ky Rkkha hai Maal Chodo Sari Me Salwar me Ky Rkkha hai`",
]
NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`Haha yes`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isnâ€™t enough to let someone know how you feel. Thatâ€™s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]
ZALG_LIST = [["Ì–",
              " Ì—",
              " Ì˜",
              " Ì™",
              " Ìœ",
              " Ì",
              " Ìž",
              " ÌŸ",
              " Ì ",
              " Ì¤",
              " Ì¥",
              " Ì¦",
              " Ì©",
              " Ìª",
              " Ì«",
              " Ì¬",
              " Ì­",
              " Ì®",
              " Ì¯",
              " Ì°",
              " Ì±",
              " Ì²",
              " Ì³",
              " Ì¹",
              " Ìº",
              " Ì»",
              " Ì¼",
              " Í…",
              " Í‡",
              " Íˆ",
              " Í‰",
              " Í",
              " ÍŽ",
              " Í“",
              " Í”",
              " Í•",
              " Í–",
              " Í™",
              " Íš",
              " ",
              ],
             [" Ì",
              " ÌŽ",
              " Ì„",
              " Ì…",
              " Ì¿",
              " Ì‘",
              " Ì†",
              " Ì",
              " Í’",
              " Í—",
              " Í‘",
              " Ì‡",
              " Ìˆ",
              " ÌŠ",
              " Í‚",
              " Íƒ",
              " Í„",
              " ÍŠ",
              " Í‹",
              " ÍŒ",
              " Ìƒ",
              " Ì‚",
              " ÌŒ",
              " Í",
              " Ì",
              " Ì‹",
              " Ì",
              " Ì½",
              " Ì‰",
              " Í£",
              " Í¤",
              " Í¥",
              " Í¦",
              " Í§",
              " Í¨",
              " Í©",
              " Íª",
              " Í«",
              " Í¬",
              " Í­",
              " Í®",
              " Í¯",
              " Ì¾",
              " Í›",
              " Í†",
              " Ìš",
              ],
             [" Ì•",
              " Ì›",
              " Í€",
              " Í",
              " Í˜",
              " Ì¡",
              " Ì¢",
              " Ì§",
              " Ì¨",
              " Ì´",
              " Ìµ",
              " Ì¶",
              " Íœ",
              " Í",
              " Íž",
              " ÍŸ",
              " Í ",
              " Í¢",
              " Ì¸",
              " Ì·",
              " Í¡",
              ]]


EMOJIS = [
    "ðŸ˜‚",
    "ðŸ˜‚",
    "ðŸ‘Œ",
    "„1¤7",
    "ðŸ’ž",
    "ðŸ‘",
    "ðŸ‘Œ",
    "ðŸ’¯",
    "ðŸŽ¶",
    "ðŸ‘€",
    "ðŸ˜‚",
    "ðŸ‘“",
    "ðŸ‘",
    "ðŸ‘",
    "ðŸ•",
    "ðŸ’¥",
    "ðŸ´",
    "ðŸ’¦",
    "ðŸ’¦",
    "ðŸ‘",
    "ðŸ†",
    "ðŸ˜©",
    "ðŸ˜",
    "ðŸ‘‰ðŸ‘Œ",
    "ðŸ‘€",
    "ðŸ‘…",
    "ðŸ˜©",
    "ðŸš°",
]

INSULT_STRINGS = [
     "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Sharam kar bsdwale,kitni bkchodi deta.`",
    "`Chup Madarhox, bilkul chup..`",
    "`Me zindagi me chunotiyo se jyda inn jese Chutiyo se pareshaan hu.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`Jaana chodu chad jake land chaat`",
    "`Yaar ajab tere nkhare,gazab tera style hain, gand dhone ki tameez nahi, haath main mobile hai`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`Youâ€™re so ugly that when you cry, the tears roll down the back of your headâ€¦just to avoid your face.`",
    "`If youâ€™re talking behind my back then youâ€™re in a perfect position to kiss my a**!.`",
]

UWUS = [
    "(ãƒ»`Ï‰Â´ãƒ„1¤7)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)âˆ â˜†",
    "(Ã´_Ã´)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(â™¥_â™„1¤7)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "Ê˜â€¿Ê„1¤7",
    "ãƒ„1¤7(-_- )ã‚„1¤7",
    "(ã£Ë˜Ú¡Ë˜Ï„1¤7)",
    "(Â´Ð¶ï½„1¤7Ï‚)",
    "( à²„1¤7 Ê–Ì¯ à²„1¤7)",
    "(Â° ÍœÊ–Í¡Â°)â•­âˆ©â•„1¤7",
    "(áµŸàº¶ï¸„1¤7 áµŸàº¶)",
    "(à¸‡ãƒ„)à¸„1¤7",
    "Êš(â€¢ï½€",
    "(ã£â–€Â¯â–„1¤7)ã„1¤7",
    "(â— ï¹â—„1¤7)",
    "( Í¡à²„1¤7 Ê–Ì¯ Í¡à²„1¤7)",
    "( à°„1¤7 ÍŸÊ– à°„1¤7)",
    "(âˆ©ï½€-Â´)âŠƒâ”â˜†ï¾Ÿ.*ï½¥ï½¡ï¾„1¤7",
    "(âŠƒï½¡â€¢Ìâ„1¤7¿â„1¤7¢Ì„1¤7ï½„1¤7)âŠ„1¤7",
    "(._.)",
    "{â€¢Ìƒ_â€¢Ìƒ}",
    "(áµ”á´¥áµ„1¤7)",
    "â™¨_â™„1¤7",
    "â¥„1¤7.â¥„1¤7",
    "Ø­Ëšà¯°Ëšã¥ ",
    "(Ò‚â—¡_â—„1¤7)",
    "Æª(Ú“×²)â€ŽÆªâ„1¤7‹â„1¤7„1¤7",
    "(ã£â„1¤7¢Ìï½¡â€¢Ì„1¤7)â™ªâ™¬",
    "â—–áµ”á´¥áµ”â—„1¤7 â™„1¤7 â™„1¤7 ",
    "(â˜žï¾Ÿãƒ®ï¾Ÿ)â˜„1¤7",
    "[Â¬Âº-Â°]Â¬",
    "(Ô¾â€„1¤7 Ô¾)",
    "(â€¢Ì„1¤7á´—â„1¤7¢Ì„1¤7)Ùˆ Ì‘Ì‘",
    "ãƒ„1¤7(Â´ã€‡`)ï¾‰â™ªâ™ªâ™ª",
    "(à¸„1¤7'Ì€-'Ì)à¸„1¤7",
    "áƒ„1¤7(â€¢Ìâ„1¤7¢Ìáƒš)",
    "Ê• â€¢ÌØˆâ„1¤7¢Ì„1¤7 â‚„1¤7",
    "â™ªâ™ª ãƒ„1¤7(Ë‡âˆ„1¤7Ë‡ )ã‚„1¤7",
    "Ñ‰ï¼ˆï¾ŸÐ”ï¾ŸÑ‰ï¼‰",
    "( Ë‡à·´Ë„1¤7 )",
    "ëˆˆ_ëˆ„1¤7",
    "(à¹‘â„1¤7¢Ì„1¤7 â‚„1¤7 â€¢Ì„1¤7à¹„1¤7) ",
    "( Ë˜ Â³Ë˜)â™„1¤7 ",
    "Ô…(â‰–â„1¤7¿â‰–Ô…)",
    "â™¥â„1¤7¿â™¥",
    "â—”_â—„1¤7",
    "â½â½à¬„1¤7( ËŠáµ•Ë„1¤7 )à¬“â¾â„1¤7",
    "ä¹„1¤7( â—„1¤7 à±ªâ—”)ã€„1¤7      â”„1¤7(ï¿£Ð„1¤7 ï¿„1¤7)â”„1¤7",
    "( à° àµ à°„1¤7 )ï¾„1¤7",
    "Ù©(à¹_à¹„1¤7)Û¶",
    "â”„1¤7(ã††ã‰¨ã†„1¤7)Êƒ",
    "à° _à°„1¤7",
    "(ã¥ï½¡â—•â„1¤7¿â„1¤7¿â—•ï½„1¤7)ã„1¤7",
    "(ãƒŽà²  âˆ©à² )ãƒŽå½¡( \\oÂ°o)\\",
    "â€œãƒ½(Â´â–½ï½€)ãƒŽâ„1¤7„1¤7",
    "à¼„1¤7 à¼Žàº¶ à·„1¤7 à¼Žàº¶à¼„1¤7",
    "ï½¡ï¾Ÿ( ï¾Ÿà®‡â€¸à®‡ï¾„1¤7)ï¾Ÿï½¡",
    "(ã¥ï¿£ Â³ï¿„1¤7)ã„1¤7",
    "(âŠ„1¤7.â˜„1¤7)7",
    "á•„1¤7( á„1¤7 )á•„1¤7",
    "t(-_-t)",
    "(à²¥âŒ£à²„1¤7)",
    "ãƒ½à¼¼ à² ç›Šà²„1¤7 à¼½ï¾‰",
    "à¼¼âˆµà¼„1¤7 à¼¼â¨à¼„1¤7 à¼¼â¢à¼„1¤7 à¼¼â¤à¼„1¤7",
    "ãƒŸâ—ï¹â˜‰ãƒ„1¤7",
    "(âŠ™_â—„1¤7)",
    "Â¿â“§_â“§ï®Œ",
    "à² _à²„1¤7",
    "(Â´ï½¥_ï½¥`)",
    "á•„1¤7(Ã²_Ã³Ë‡)á•„1¤7",
    "âŠ™ï¹âŠ„1¤7",
    "(â•¯Â°â–¡Â°ï¼‰â•¯ï¸„1¤7 â”»â”â”„1¤7",
    r"Â¯\_(âŠ™ï¸¿âŠ„1¤7)_/Â¯",
    "Ù©â—”Ì¯â—”Û¶",
    "Â°â€¿â„1¤7¿Â„1¤7",
    "á•„1¤7(â‡„1¤7â€¸â†¼â€„1¤7)á•„1¤7",
    "âŠ„1¤7(â—‰â„1¤7¿â—‰)ã„1¤7",
    "Vâ€¢á´¥â€¢V",
    "q(â‚â„1¤7¿â‚)p",
    "à²¥_à²„1¤7",
    "à¸…^â€¢ï»Œâ€¢^à¸„1¤7",
    "à²¥ï¹à²„1¤7",
    "ï¼„1¤7 ^_^ï¼‰oè‡ªè‡ªoï¼ˆ^_^ ï¼„1¤7",
    "à² â„1¤7¿à² ",
    "ãƒ„1¤7(Â´â–½`)/",
    "áµ’á´¥áµ„1¤7#",
    "( Í¡Â° ÍœÊ– Í¡Â°)",
    "â”¬â”€â”¬ï»¿ ãƒ„1¤7( ã‚„1¤7-ã‚œãƒŽ)",
    "ãƒ„1¤7(Â´ãƒ¼ï½€)ãƒ„1¤7",
    "â˜„1¤7(âŒ’â–½âŒ„1¤7)â˜„1¤7",
    "Îµ=Îµ=Îµ=â”„1¤7(;*Â´Ð”`)ï¾„1¤7",
    "(â•„1¤7 à² ç›Šà²„1¤7)",
    "â”¬â”€â”¬âƒ°Í¡â€„1¤7(áµ”áµ•áµ”Íœâ„1¤7„1¤7)",
    "â”»â”â”„1¤7 ï¸µãƒ½(`Ð”Â´)ï¾‰ï¸µï»„1¤7 â”»â”â”„1¤7",
    r"Â¯\_(ãƒ„1¤7)_/Â¯",
    "Ê•áµ”á´¥áµ”Ê„1¤7",
    "(`ï½¥Ï‰ï½¥Â´)",
    "Ê•â€¢á´¥â€¢Ê„1¤7",
    "áƒ„1¤7(ï½„1¤7ãƒ¼Â´áƒš)",
    "Ê•Ê˜Ì…ÍœÊ˜Ì…Ê”",
    "ï¼ˆã„1¤7„1¤7ï¾ŸÐ”ï¾Ÿï¼„1¤7",
    r"Â¯\(Â°_o)/Â¯",
    "(ï½¡â—•â€¿â—•ï½„1¤7)",
]

RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs far, far away from earth`",
    "`Running faster than supercomputer, cuzwhynot`",
    "`Runs to SunnyLeone`",
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
    "`Running a marathon...there's an app for that.`",
]

RAPE_STRINGS = [
     "`Rape Done Drink The Cum`",
     "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",
     "`The user has been successfully raped`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
     "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
     "`Rape coming... Raped! haha ðŸ˜†`",
     "`Kitni baar Rape krvyega mujhse?`",
     "`Tu Randi hai Sabko pta haiðŸ˜‚`",
     "`Don't rape too much bossdk, else problem....`",
     "`Tu sasti rendi hai Sabko pta haiðŸ˜‚`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 
ABUSE_STRINGS = [
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Muh Me Lega Bhosdike ?`",
	   "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari humðŸ˜‚`",
       "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
       "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
       "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",
       "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
]
GEY_STRINGS = [
     "`you gey bsdk`",
     "`you gey`",
     "`you gey in the house`",
     "`you chakka`",
     "`Bhago BC! Chakka aya`",
     "`you gey gey gey gey gey gey gey gey`",
     "`you gey go away`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Proness Lebel: 6969696969`",
     "`Itna pro banda dekhlia bc, ab to marna hoga.`",
     "`U iz pro but i iz ur DAD, KeK`",
     "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
     "`Sometimes one middle finger isnÃ¢â‚¬â„¢t enough to let someone know how you feel. ThatÃ¢â‚¬â„¢s why you have two hands`",
     "`Some Nimbas need to open their small minds instead of their big mouths`",
     "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
     "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
     "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",

]
CHU_STRINGS = [
     "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
     "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
     "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata haiðŸ˜‚.`",
     "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
     "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
     "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
     "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
]
FUK_STRINGS = [
   "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
   "`Talking to a liberal is like trying to explain social media to a 70 years old`",
   "`CHAND PE HAI APUN LAWDE.`",
   "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
   "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",
   "`Cachaa Ooo bhosdi wale Chacha`",
   "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
   "`Nachoo Bhosdike Nachoo`",
   "`Jinda toh jaat ke baal bhi hai`",
   "`Sab ko pta tu randi ka baccha hai (its just a joke)`", 
]
THANOS_STRINGS = [
     "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
     "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
     "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
     "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
     "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
     "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta haiðŸ˜‚`",
     "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
     "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chuttiðŸ˜›`",
     "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
     "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
ABUSEHARD_STRING = [
	"`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
	"`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
	"`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
        "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
        "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata haiðŸ˜‚.`",
        "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
        "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
        "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
	"`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
        "`Pani kam hai matke me gand marlunga jhatke me.`",
        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta haiðŸ˜‚`",
        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chuttiðŸ˜›`",
        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
HELLOSTR = [
    "`Hi !`",
    "`â€˜Ello, gov'nor!`",
    "`Whatâ€™s crackinâ€„1¤7?`",
    "`â€˜Sup, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`Hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`Hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`Whatâ€™s kickinâ€„1¤7, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh retarded gey! Well Hello`",
]

SHGS = [
    "â”„1¤7(Â´Ð´ï½„1¤7)â”„1¤7",
    "â”„1¤7(Â´ï½žï½€)â”„1¤7",
    "â”„1¤7(Â´ãƒ¼ï½€)â”„1¤7",
    "â”„1¤7(ï¿£ãƒ˜ï¿„1¤7)â”„1¤7",
    "â•„1¤7(â•¯âˆ€â•„1¤7)â•„1¤7",
    "â•„1¤7(â•¯_â•„1¤7)â•„1¤7",
    "â”„1¤7(Â´Ð´`)â”„1¤7",
    "â”„1¤7(Â´âˆ„1¤7ï½„1¤7)â”„1¤7",
    "Ê…(Ìâ—¡â—)Êƒ",
    "áƒ„1¤7(ï¾ŸÐ´ï¾Ÿáƒ„1¤7)",
    "â”„1¤7(ï¾Ÿï½žï¾„1¤7)â”„1¤7",
    "â”„1¤7('Ð´')â”„1¤7",
    "áƒšï½œï¼¾Ð”ï¼¾áƒšï½œ",
    "áƒšï¼ˆâ•¹Îµâ•¹áƒšï¼‰",
    "áƒ„1¤7(à² ç›Šà²„1¤7)áƒ„1¤7",
    "â”„1¤7(â€˜ï½ž`;)â”„1¤7",
    "ãƒ„1¤7(Â´ï¼ï½€;)ãƒ„1¤7",
    "â”„1¤7( -â€„1¤7-)â”„1¤7",
    "ä¹à¼¼â˜¯â„1¤7¿â˜¯âœ¿à¼½ã„„1¤7",
    "Ê…ï¼ˆÂ´â—”à±ªâ—”ï¼‰Ê„1¤7",
    "áƒ„1¤7(â€¢Ï„1¤7 â€¢áƒš)",
    "ãƒ„1¤7(ã‚œï½žã‚œo)ãƒ„1¤7",
    "ãƒ„1¤7(~ï½ž~ )ãƒ„1¤7",
    "â”„1¤7(~ãƒ¼~;)â”„1¤7",
    "â”„1¤7(-ã€‚ãƒ¼;)â”„1¤7",
    "Â¯\_(ãƒ„1¤7)_/Â¯",
    "Â¯\_(âŠ™_Ê–âŠ„1¤7)_/Â¯",
    "ä¹Ê„1¤7 â€¢Ì„1¤7 Û â€¢Ì„1¤7 Ê”ã„„1¤7",
    "Â¯\_à¼„1¤7 à²„1¤7 â€„1¤7 à²„1¤7 à¼½_/Â¯",
    "ä¹„1¤7( â°Í„1¤7  Ä¹Ì¯ â°Í„1¤7 ) ã„„1¤7",
]

CRI = [
    "Ø£â€¿Ø„1¤7",
    "â•¥ï¹â•„1¤7",
    "(;ï¹„1¤7;)",
    "(ToT)",
    "(â”³Ð”â”³)",
    "(à²¥ï¹à²„1¤7)",
    "ï¼ˆï¼›ã¸ï¼šï¼„1¤7",
    "(Tï¼¿T)",
    "ï¼ˆÏ„1¤7ãƒ¼Ï„1¤7ï¼„1¤7",
    "(ï¼´â–½ï¼„1¤7)",
    "(â‹Ÿï¹â‹„1¤7)",
    "ï¼ˆï½‰Ð”ï½‰ï¼‰",
    "(Â´Ð”âŠ‚ãƒ½",
    "(;Ð”;)",
    "ï¼„1¤7>ï¹„1¤7<ï¼„1¤7",
    "(TÐ´T)",
    "(ã¤ï¹âŠ„1¤7)",
    "à¼¼â˜¯ï¹â˜¯à¼„1¤7",
    "(ãƒŽï¹ãƒ„1¤7)",
    "(ãƒŽAãƒ„1¤7)",
    "(â•¥_â•„1¤7)",
    "(TâŒ“T)",
    "(à¼Žàº¶âŒ‘à¼Žàº„1¤7)",
    "(â˜ï¹â„1¤7)ï½„1¤7",
    "(à²¥_Ê–à²„1¤7)",
    "(ã¤Ð´âŠ‚)",
    "(â‰–Íž_â‰–Ì„1¤7)",
    "(à®‡ï¹à®‡`ï½„1¤7)",
    "à¼¼à²¢_à²¢à¼½",
    "à¼„1¤7 à¼Žàº¶ à·„1¤7 à¼Žàº¶à¼„1¤7",
]

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "{throws} a {item} at {victim}.",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "ties {victim} to a chair and {throws} a {item} at them.",
    "gave a friendly push to help {victim} learn to swim in lava."
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "fek ke maari",
    "slaps",
    "smacks",
    "bashes",
]

# ===========================================


#@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
@borg.on(admin_cmd(pattern=r"(\w+)say (.*)"))
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', 'Â´')}`")


@register(outgoing=True, pattern="^.:/$")
async def kek(keks):
    if not keks.text[0].isalpha() and keks.text[0] not in ("/", "#", "@", "!"):
        """ Check yourself ;)"""
        uio = ["/", "\\"]
        for i in range(1, 15):
            time.sleep(0.3)
            await keks.edit(":" + uio[i % 2])


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        """ slaps a user, or get slapped if not a reply. """
        if event.fwd_from:
            return

        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id

        if not message_id_to_reply:
            message_id_to_reply = None

        try:
            await event.edit(caption)

        except:
            await event.edit("`Can't slap this person, need to fetch some sticks and stones !!`")

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None

    return replied_user

async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = "..." + temp.format(victim=slapped, item=item, hits=hit, throws=throw)

    return caption

@register(outgoing=True, pattern="^.-_-$")
async def lol(lel):
    if not lel.text[0].isalpha() and lel.text[0] not in ("/", "#", "@", "!"):
        """ Ok... """
        okay = "-_-"
        for _ in range(10):
            okay = okay[:-1] + "_-"
            await lel.edit(okay)

 
@register(outgoing=True, pattern="^.;_;$")
async def fun(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = ";__;"
        for j in range(10):
            t = t[:-1] + "_;"
            await e.edit(t)

@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(CRI))

@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(INSULT_STRINGS))

@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`ðŸ˜‚ðŸ…±ï¸IvEðŸ‘sOMEðŸ‘…textðŸ‘…forâœŒï¸MeðŸ‘ŒtOðŸ‘MAkEðŸ‘€iTðŸ’žfunNy!ðŸ’¦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with ðŸ…±ï¸„1¤7
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "ðŸ…±ï¸„1¤7"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`ï¼§ï½‰ï½–ï½… ï½“ï½ï½ï½… ï½”ï½…ï½˜ï½” ï½†ï½ï½„1¤7 ï½–ï½ï½ï½ï½’ï¼`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await vpr.edit("".join(reply_text))

			  
@register(outgoing=True, pattern="^.repo$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Click [here](https://github.com/hackelite01/Marcususerbot.git) to open this cool userbot repo.")
			  
			  
@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUï½ï½…ï½‰ï½ï½•ï¼¡ï¼¥ï¼©ï¼¯ï¼µÐ°ÐµÐ¸Ð¾ÑƒÑŽÑÑ‹ÑÑ‘])",
            (r"\1"*count),
            message
        )
        await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit(
                "`gÍ« Ì† iÌ› Ìº vÍ‡Ì† eÌÍ…   aÌ¢Í¦   sÌ´Ìª cÌ¢Ì¸ aÌ¸Ìˆ rÍ©Í£ yÍ–Íž   tÌ¨Íš eÌ Ì xÌ¢Í–  tÍ›Í”`"
            )
            return

        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue

            for _ in range(0, 3):
                randint = random.randint(0, 2)

                if randint == 0:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[2]).strip()

            reply_text.append(charac)

        await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ Greet everyone! """
    if not hello.text[0].isalpha() and hello.text[0] not in ("/", "#", "@", "!"):
        await hello.edit(random.choice(HELLOSTR))
			  
@register(outgoing=True, pattern="^.pkill$")
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                "`Targeted user killed by Headshot ðŸ˜ˆ......`\n"
		"#Sad_Reacts_Onli\n"
            )
			  
@register(outgoing=True, pattern="^.bt$")
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await bte.edit(
                "`BLUETEXT MUST CLICK.`\n"
                "`Are you a stupid animal which is attracted to colours?`"
            )
			  
@register(outgoing=True, pattern="^.rape$")
async def raping (raped):
    """ Dont Rape Too much -_-"""
    if not raped.text[0].isalpha() and raped.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(RAPE_STRINGS) - 1)
        reply_text = RAPE_STRINGS[index]
        await raped.edit(reply_text)
			  
@register(outgoing=True, pattern="^.pro$")
async def proo (pros):
    """ String for Pros only -_-"""
    if not pros.text[0].isalpha() and pros.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(PRO_STRINGS) - 1)
        reply_text = PRO_STRINGS[index]
        await pros.edit(reply_text)

@register(outgoing=True, pattern="^.fuk$")
async def chutiya (fuks):
    """ String for fhu only -_-"""
    if not fuks.text[0].isalpha() and fuks.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = FUK_STRINGS[index]
        await fuks.edit(reply_text)

@register(outgoing=True, pattern="^.chu$")
async def chutiya (chus):
    """ String for Chu only -_-"""
    if not chus.text[0].isalpha() and chus.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = CHU_STRINGS[index]
        await chus.edit(reply_text)
			  			  
@register(outgoing=True, pattern="^.thanos$")
async def thanos (thanos):
    """ String for thanos only -_-"""
    if not thanos.text[0].isalpha() and thanos.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(THANOS_STRINGS) - 1)
        reply_text = THANOS_STRINGS[index]
        await thanos.edit(reply_text)	
			  
@register(outgoing=True, pattern="^.hardabuse$")
async def fuckedd (abusehard):
    """ Dont Use this Too much bsdk -_-"""
    if not abusehard.text[0].isalpha() and abusehard.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSEHARD_STRING) - 1)
        reply_text = ABUSEHARD_STRING[index]
        await abusehard.edit(reply_text)
			  
			  
@register(outgoing=True, pattern="^.gey$")
async def geys (geyed):
    """ Use only for gey ppl -_-"""
    if not geyed.text[0].isalpha() and geyed.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(GEY_STRINGS) - 1)
        reply_text = GEY_STRINGS[index]
        await geyed.edit(reply_text)
			  
			  
@register(outgoing=True, pattern="^.abuse$")
async def abusing (abused):
    """ Dont Abuse Too much bsdk -_-"""
    if not abused.text[0].isalpha() and abused.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSE_STRINGS) - 1)
        reply_text = ABUSE_STRINGS[index]
        await abused.edit(reply_text)


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await owo.edit("` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in ("/", "#", "@", "!"):
        await react.edit(random.choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" Â¯\_(ãƒ„1¤7)_/Â¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(random.choice(SHGS))




@register(outgoing=True, pattern="^.noob$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in ("/", "#", "@", "!"):
        await hahayes.edit(random.choice(NOOBSTR))
			  
@register(outgoing=True, pattern="^.rendi$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in ("/", "#", "@", "!"):
        await hahayes.edit(random.choice(RENDISTR))
			 			  
@register(outgoing=True, pattern="^.oof$")
async def Oof(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = "Oof"
        for j in range(15):
            t = t[:-1] + "of"
            await e.edit(t)

@register(outgoing=True, pattern="^.10iq$")
async def iqless(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("â™„1¤7")




@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "ðŸ‘ "
        reply_text += message.replace(" ", " ðŸ‘ ")
        reply_text += " ðŸ‘"
        await memereview.edit(reply_text)




@register(outgoing=True, pattern="^.smk (.*)")
async def smrk(smk):
        if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
            textx = await smk.get_reply_message()
            message = smk.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        if message == 'dele':
            await smk.edit( message +'te the hell' + "ãƒ„1¤7" )
            await smk.edit("ãƒ„1¤7")
        else:
             smirk = " ãƒ„1¤7"
             reply_text = message + smirk
             await smk.edit(reply_text)





@register(outgoing=True, pattern="^.lfy (.*)",)
async def let_me_google_that_for_you(lmgtfy_q):
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] not in ("/", "#", "@", "!"):
        textx = await lmgtfy_q.get_reply_message()
        query = lmgtfy_q.text
        if query[5:]:
            query = str(query[5:])
        elif textx:
            query = textx
            query = query.message
        query_encoded = query.replace(" ", "+")
        lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
        payload = {'format': 'json', 'url': lfy_url}
        r = requests.get('http://is.gd/create.php', params=payload)
        await lmgtfy_q.edit(f"[{query}]({r.json()['shorturl']})")
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "LMGTFY query `" + query + "` was executed successfully",
            )



               
			  

            
			  

CMD_HELP.update({
    "memes": ".cowsay\
\nUsage: cow which says things.\
\n\n.milksay\
\nUsage: Weird Milk that can speak\
\n\n:/\
\nUsage: Check yourself ;)\
\n\n-_-\
\nUsage: Ok...\
\n\n;_;\
\nUsage: Like `-_-` but crying.\
\n\n.cp\
\nUsage: Copypasta the famous meme\
\n\n.vapor\
\nUsage: Vaporize everything!\
\n\n.str\
\nUsage: Stretch it.\
\n\n.10iq\
\nUsage: You retard !!\
\n\n.zal\
\nUsage: Invoke the feeling of chaos.\
\n\n.oof\
\nUsage: Ooooof\
\n\n.moon\
\nUsage: kensar moon animation.\
\n\n.clock\
\nUsage: kensar clock animation.\
\n\n.earth\
\nUsage: kensar earth animation.\
\n\n.hi\
\nUsage: Greet everyone!\
\n\n.coinflip <heads/tails>\
\nUsage: Flip a coin !!\
\n\n.owo\
\nUsage: UwU\
\n\n.react\
\nUsage: Make your userbot react to everything.\
\n\n.slap\
\nUsage: reply to slap them with random objects !!\
\n\n.cry\
\nUsage: y u du dis, i cri.\
\n\n.shg\
\nUsage: Shrug at it !!\
\n\n.runs\
\nUsage: Run, run, RUNNN! [`.disable runs`: disable | `.enable runs`: enable]\
\n\n.metoo\
\nUsage: Haha yes\
\n\n.mock\
\nUsage: Do it and find the real fun.\
\n\n.clap\
\nUsage: Praise people!\
\n\n.f <emoji/character>\
\nUsage: Pay Respects.\
\n\n.bt\
\nUsage: Believe me, you will find this useful.\
\n\n.smk <text/reply>\
\nUsage: A shit module for ãƒ„1¤7 , who cares.\
\n\n.type\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n.lfy <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n.decide\
\nUsage: Make a quick decision.\
\n\n.abusehard\
\nUsage: You already got that! Ain't?.\
\n\n.chu\
\nUsage: Incase, the person infront of you is....\
\n\n.fuk\
\nUsage: The onlu word that can be used fucking everywhere.\
\n\n.thanos\
\nUsage: Try and then Snap.\
\n\n.noob\
\nUsage: Whadya want to know? Are you a NOOB?\
\n\n.pro\
\nUsage: If you think you're pro, try this.\
\n\n.abuse\
\nUsage: Protects you from unwanted peeps.\
\n\n\nThanks to ðŸ…±ï¸ottomðŸ…±ï¸extðŸ…±ï¸ot (@NotAMemeBot) for some of these."
})
