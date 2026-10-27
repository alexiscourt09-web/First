import os
from datetime import time
from zoneinfo import ZoneInfo

import discord
from discord.ext import tasks

# ====== CONFIG ======
TOKEN = os.getenv("DISCORD_TOKEN") or "COLLE_TON_TOKEN_ICI"
CHANNEL_ID = 1507324308144263259
TIMEZONE = ZoneInfo("Europe/Paris")
# ====================


class Bot(discord.Client):
    async def setup_hook(self):
        midnight_first.start()

    async def on_ready(self):
        print(f"Connecté en tant que {self.user}")


bot = Bot(intents=discord.Intents.default())


@tasks.loop(time=time(hour=0, minute=0, tzinfo=TIMEZONE))
async def midnight_first():
    channel = bot.get_channel(CHANNEL_ID) or await bot.fetch_channel(CHANNEL_ID)
    await channel.send("First")


bot.run(TOKEN)
