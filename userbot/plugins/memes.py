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
    "`Sellers Nasa calling Uh bhay馃槅`",
    "`Badwoo ki yojna behan bna ke ch*da uh iz badwa its your yozja?`",
    "`CHAND PE CHADA HAI CHANDYAAN KA GHODA TERA NAAM HAI MANSUR TU HAI BEHAN KA LOD*馃槀`",
    "`Jab se dil lga baithe tanhai me maa chu*da baithe wo kho gyi kisi aur ke pyar hum apne hi jaato me aag lga baithe`",
    "`Chadii ke ander se lal pani kha se ata hai ky teri masuka ka bhosda bhi paan khata hai馃槀`",
    "`Sun bhosdi ke By anonyCrew MOHABBAT KE SIWA AUR BHI GAM HAI JAMANE ME BSDK GAND PAHAT JATI HAI PAISA KAMANE ME`",
    "`Thaan liya tha Sayri nhi krege Unka pichwada dekha Alfaaz nikal gye`",
    "`Ravivaar ko dekha Chand Ka Tukra Itna Baar Dekha par Jaath na Ukra`",
    "`Katal kro Tir se Talwar me Ky Rkkha hai Maal Chodo Sari Me Salwar me Ky Rkkha hai`",
]
NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`Haha yes`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isn鈥檛 enough to let someone know how you feel. That鈥檚 why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]
ZALG_LIST = [["號",
              " 虠",
              " 虡",
              " 虣",
              " 虦",
              " 虧",
              " 虨",
              " 虩",
              " 虪",
              " 踏",
              " 胎",
              " 苔",
              " 泰",
              " 酞",
              " 太",
              " 态",
              " 汰",
              " 坍",
              " 摊",
              " 贪",
              " 瘫",
              " 滩",
              " 坛",
              " 坦",
              " 毯",
              " 袒",
              " 碳",
              " 蛥",
              " 蛧",
              " 蛨",
              " 蛪",
              " 蛵",
              " 蛶",
              " 蛽",
              " 蛿",
              " 蜁",
              " 蜄",
              " 蜋",
              " 蜌",
              " ",
              ],
             [" 虓",
              " 處",
              " 虅",
              " 虆",
              " 炭",
              " 虘",
              " 虇",
              " 虗",
              " 蛼",
              " 蜅",
              " 蛻",
              " 虈",
              " 虉",
              " 虋",
              " 蛡",
              " 蛢",
              " 蛣",
              " 蛫",
              " 蛬",
              " 蛯",
              " 虄",
              " 虃",
              " 虒",
              " 蛺",
              " 虂",
              " 虌",
              " 虖",
              " 探",
              " 虊",
              " 停",
              " 亭",
              " 庭",
              " 挺",
              " 艇",
              " 通",
              " 桐",
              " 酮",
              " 瞳",
              " 同",
              " 铜",
              " 彤",
              " 童",
              " 叹",
              " 蜎",
              " 蛦",
              " 虤",
              ],
             [" 虝",
              " 虥",
              " 蛝",
              " 蛠",
              " 蜆",
              " 獭",
              " 挞",
              " 抬",
              " 台",
              " 檀",
              " 痰",
              " 潭",
              " 蜏",
              " 蜐",
              " 蜑",
              " 蜔",
              " 蜖",
              " 廷",
              " 谈",
              " 谭",
              " 汀",
              ]]


EMOJIS = [
    "馃槀",
    "馃槀",
    "馃憣",
    "鉁�",
    "馃挒",
    "馃憤",
    "馃憣",
    "馃挴",
    "馃幎",
    "馃憖",
    "馃槀",
    "馃憮",
    "馃憦",
    "馃憪",
    "馃崟",
    "馃挜",
    "馃嵈",
    "馃挦",
    "馃挦",
    "馃崙",
    "馃崋",
    "馃槱",
    "馃槒",
    "馃憠馃憣",
    "馃憖",
    "馃憛",
    "馃槱",
    "馃毎",
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
    "`You鈥檙e so ugly that when you cry, the tears roll down the back of your head鈥ust to avoid your face.`",
    "`If you鈥檙e talking behind my back then you鈥檙e in a perfect position to kiss my a**!.`",
]

UWUS = [
    "(銉籤蠅麓銉�)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)鈭犫槅",
    "(么_么)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(鈾鈾�)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "蕵鈥渴�",
    "銉�(-_- )銈�",
    "(銇Ｋ樬∷樝�)",
    "(麓卸锝�蟼)",
    "( 嗖� 蕱摊 嗖�)",
    "(掳 蜏蕱汀掳)鈺埄鈺�",
    "(岬熰憾锔� 岬熰憾)",
    "(喔囥儎)喔�",
    "蕷(鈥絸",
    "(銇ｂ杸炉鈻�)銇�",
    "(鈼狅箯鈼�)",
    "( 汀嗖� 蕱摊 汀嗖�)",
    "( 喟� 蜔蕱 喟�)",
    "(鈭╋絸-麓)鈯冣攣鈽嗭緹.*锝ワ健锞�",
    "(鈯冿健鈥⑻佲�库�⑻�锝�)鈯�",
    "(._.)",
    "{鈥⑻僟鈥⑻儅",
    "(岬斸触岬�)",
    "鈾╛鈾�",
    "猊�.猊�",
    "丨藲喁八氥仴 ",
    "(覀鈼鈼�)",
    "篇(趽撞)鈥幤�嬧��",
    "(銇ｂ�⑻侊健鈥⑻�)鈾櫖",
    "鈼栣禂岽メ禂鈼� 鈾� 鈾� ",
    "(鈽烇緹銉緹)鈽�",
    "[卢潞-掳]卢",
    "(跃鈥� 跃)",
    "(鈥⑻�岽椻�⑻�)賵 虘虘",
    "銉�(麓銆嘸)锞夆櫔鈾櫔",
    "(喔�'虁-'虂)喔�",
    "醿�(鈥⑻佲�⑻佱儦)",
    "蕰 鈥⑻佖堚�⑻� 鈧�",
    "鈾櫔 銉�(藝鈭�藝 )銈�",
    "褖锛堬緹袛锞熝夛級",
    "( 藝喾此� )",
    "雸坃雸�",
    "(喙戔�⑻� 鈧� 鈥⑻�喙�) ",
    "( 藰 鲁藰)鈾� ",
    "詤(鈮栤�库墫詤)",
    "鈾モ�库櫏",
    "鈼擾鈼�",
    "鈦解伣喱�( 藠岬曀� )喱撯伨鈦�",
    "涔�( 鈼� 啾棓)銆�      鈹�(锟Ｐ� 锟�)鈹�",
    "( 喟犩禒喟� )锞�",
    "侃(喙廮喙�)鄱",
    "鈹�(銌嗐墾銌�)蕛",
    "喟燺喟�",
    "(銇ワ健鈼曗�库�库棔锝�)銇�",
    "(銉庎矤 鈭┼矤)銉庡健( \\o掳o)\\",
    "鈥溿兘(麓鈻斤絸)銉庘��",
    "嗉� 嗉庎憾 喾� 嗉庎憾嗉�",
    "锝★緹( 锞熰畤鈥膏畤锞�)锞燂健",
    "(銇ワ浚 鲁锟�)銇�",
    "(鈯�.鈽�)7",
    "釙�( 釔� )釙�",
    "t(-_-t)",
    "(嗖モ專嗖�)",
    "銉洁技 嗖犵泭嗖� 嗉斤緣",
    "嗉尖埖嗉� 嗉尖崹嗉� 嗉尖崲嗉� 嗉尖崵嗉�",
    "銉熲棌锕忊槈銉�",
    "(鈯檁鈼�)",
    "驴鈸鈸э畬",
    "嗖燺嗖�",
    "(麓锝锝)",
    "釙�(貌_贸藝)釙�",
    "鈯欙箯鈯�",
    "(鈺扳枴掳锛夆暞锔� 鈹烩攣鈹�",
    r"炉\_(鈯欙缚鈯�)_/炉",
    "侃鈼斕棓鄱",
    "掳鈥库�柯�",
    "釙�(鈬�鈥糕喖鈥�)釙�",
    "鈯�(鈼夆�库棄)銇�",
    "V鈥⑨触鈥",
    "q(鉂傗�库潅)p",
    "嗖嗖�",
    "喔區鈥粚鈥喔�",
    "嗖ワ箯嗖�",
    "锛� ^_^锛塷鑷嚜o锛坁_^ 锛�",
    "嗖犫�苦矤",
    "銉�(麓鈻絗)/",
    "岬掅触岬�#",
    "( 汀掳 蜏蕱 汀掳)",
    "鈹攢鈹豢 銉�( 銈�-銈溿儙)",
    "銉�(麓銉硷絸)銉�",
    "鈽�(鈱掆柦鈱�)鈽�",
    "蔚=蔚=蔚=鈹�(;*麓袛`)锞�",
    "(鈺� 嗖犵泭嗖�)",
    "鈹攢鈹儼汀鈥�(岬斸禃岬斖溾��)",
    "鈹烩攣鈹� 锔点兘(`袛麓)锞夛傅锘� 鈹烩攣鈹�",
    r"炉\_(銉�)_/炉",
    "蕰岬斸触岬斒�",
    "(`锝ハ夛渐麓)",
    "蕰鈥⑨触鈥⑹�",
    "醿�(锝�銉悸瘁儦)",
    "蕰蕵虆蜏蕵虆蕯",
    "锛堛��锞熜旓緹锛�",
    r"炉\(掳_o)/炉",
    "(锝♀棔鈥库棔锝�)",
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
     "`Rape coming... Raped! haha 馃槅`",
     "`Kitni baar Rape krvyega mujhse?`",
     "`Tu Randi hai Sabko pta hai馃槀`",
     "`Don't rape too much bossdk, else problem....`",
     "`Tu sasti rendi hai Sabko pta hai馃槀`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 
ABUSE_STRINGS = [
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Muh Me Lega Bhosdike ?`",
	   "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum馃槀`",
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
     "`Sometimes one middle finger isn芒鈧劉t enough to let someone know how you feel. That芒鈧劉s why you have two hands`",
     "`Some Nimbas need to open their small minds instead of their big mouths`",
     "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
     "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
     "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",

]
CHU_STRINGS = [
     "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
     "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
     "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai馃槀.`",
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
     "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai馃槀`",
     "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
     "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti馃槢`",
     "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
     "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
ABUSEHARD_STRING = [
	"`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
	"`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
	"`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
        "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
        "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai馃槀.`",
        "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
        "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
        "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
	"`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
        "`Pani kam hai matke me gand marlunga jhatke me.`",
        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai馃槀`",
        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti馃槢`",
        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
HELLOSTR = [
    "`Hi !`",
    "`鈥楨llo, gov'nor!`",
    "`What鈥檚 crackin鈥�?`",
    "`鈥楽up, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`Hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`Hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`What鈥檚 kickin鈥�, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh retarded gey! Well Hello`",
]

SHGS = [
    "鈹�(麓写锝�)鈹�",
    "鈹�(麓锝烇絸)鈹�",
    "鈹�(麓銉硷絸)鈹�",
    "鈹�(锟ｃ儤锟�)鈹�",
    "鈺�(鈺垁鈺�)鈺�",
    "鈺�(鈺痏鈺�)鈺�",
    "鈹�(麓写`)鈹�",
    "鈹�(麓鈭�锝�)鈹�",
    "蕝(虂鈼♀棟)蕛",
    "醿�(锞熜达緹醿�)",
    "鈹�(锞燂綖锞�)鈹�",
    "鈹�('写')鈹�",
    "醿氾綔锛拘旓季醿氾綔",
    "醿氾紙鈺刮碘暪醿氾級",
    "醿�(嗖犵泭嗖�)醿�",
    "鈹�(鈥橈綖`;)鈹�",
    "銉�(麓锛嶏絸;)銉�",
    "鈹�( -鈥�-)鈹�",
    "涔佮技鈽�库槸鉁苦冀銊�",
    "蕝锛埪粹棓啾棓锛壥�",
    "醿�(鈥⑾� 鈥⑨儦)",
    "銉�(銈滐綖銈渙)銉�",
    "銉�(~锝瀪 )銉�",
    "鈹�(~銉紐;)鈹�",
    "鈹�(-銆傘兗;)鈹�",
    "炉\_(銉�)_/炉",
    "炉\_(鈯檁蕱鈯�)_/炉",
    "涔伿� 鈥⑻� 蹪 鈥⑻� 蕯銊�",
    "炉\_嗉� 嗖� 鈥� 嗖� 嗉絖/炉",
    "涔�( 鈦巴�  墓摊 鈦巴� ) 銊�",
]

CRI = [
    "兀鈥控�",
    "鈺ワ箯鈺�",
    "(;锕�;)",
    "(ToT)",
    "(鈹承斺敵)",
    "(嗖ワ箯嗖�)",
    "锛堬紱銇革細锛�",
    "(T锛縏)",
    "锛埾�銉枷�锛�",
    "(锛粹柦锛�)",
    "(鈰燂箯鈰�)",
    "锛堬綁袛锝夛級",
    "(麓袛鈯傘兘",
    "(;袛;)",
    "锛�>锕�<锛�",
    "(T写T)",
    "(銇わ箯鈯�)",
    "嗉尖槸锕忊槸嗉�",
    "(銉庯箯銉�)",
    "(銉嶢銉�)",
    "(鈺鈺�)",
    "(T鈱揟)",
    "(嗉庎憾鈱戉紟嗪�)",
    "(鈽嶏箯鈦�)锝�",
    "(嗖蕱嗖�)",
    "(銇ば粹妭)",
    "(鈮柾瀇鈮柼�)",
    "(喈囷箯喈嘸锝�)",
    "嗉监并_嗖⑧冀",
    "嗉� 嗉庎憾 喾� 嗉庎憾嗉�",
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

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '麓')}`")


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
            await cp_e.edit("`馃槀馃叡锔廔vE馃憪sOME馃憛text馃憛for鉁岋笍Me馃憣tO馃憪MAkE馃憖iT馃挒funNy!馃挦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 馃叡锔�
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "馃叡锔�"
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
            await vpr.edit("`锛э綁锝栵絽 锝擄綇锝嶏絽 锝旓絽锝橈綌 锝嗭綇锝� 锝栵絹锝愶綇锝掞紒`")
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
            r"([aeiouAEIOU锝侊絽锝夛綇锝曪肌锛ワ缉锛嫉邪械懈芯褍褞褟褘褝褢])",
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
                "`g瞳 虇 i虥 毯 v蛧虇 e虖蛥   a挞挺   s檀酞 c挞谈 a谈虉 r桐停 y蜄蜑   t台蜌 e虪虂 x挞蜄  t蜎蛿`"
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
                "`Targeted user killed by Headshot 馃槇......`\n"
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
    r""" 炉\_(銉�)_/炉 """
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
        await e.edit("鈾�")




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
        reply_text = "馃憦 "
        reply_text += message.replace(" ", " 馃憦 ")
        reply_text += " 馃憦"
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
            await smk.edit( message +'te the hell' + "銉�" )
            await smk.edit("銉�")
        else:
             smirk = " 銉�"
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
\nUsage: A shit module for 銉� , who cares.\
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
\n\n\nThanks to 馃叡锔弌ttom馃叡锔廵xt馃叡锔弌t (@NotAMemeBot) for some of these."
})
