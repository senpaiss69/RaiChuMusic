## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQATTtuuqyndWWqINhBR8DpOOdS4i6TBYIu3vtbIpDvpGB2iTIccX8bPyrnoMbXmptqmpub4DLv4h5RTp1CWweGn7PHM0EzqRi7pkf36PCSej2KyrMOvO5q2HSH4Azz8F81SNoZwN3pLOeon_5MhDmbliK2UMakEbpQuZ_P6vjygaJs67BLhjZ2Y2_4fj9YAlwolBa53iJwxToKPymDzY7HpLNQrO0xmXWh8kMKC8zjzrn1nndDzY8qrR_3vpWNGv_zXpw6NJGMfS4yiKNlEj2xbmL2V-AUNIGwNjoqCsGK8FJMa2dwpVMf3ElLqcAGEZy-hIIfJoBbVs3SRzASuLb1HAAAAAS0BYg0A")
BOT_TOKEN = getenv("5604653078:AAHuhmcSGDoPsMYVpzE5HGLj-MU9B7qf-Y4")
BOT_NAME = getenv("uzakimusicBot")
API_ID = int(getenv("API_ID", "2966409"))
API_HASH = getenv("API_HASH", "98f2449a6df6a2e97a29f3804ead4416")
OWNER_NAME = getenv("OWNER_NAME", "senpais69")
ALIVE_NAME = getenv("ALIVE_NAME", "Uzaki")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "okayvhai")
BOT_USERNAME = getenv("UzakiMusic69_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "senpais69")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("5050032653").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
