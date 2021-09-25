import os
from discord import activity
from discord.enums import ActivityType
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(","),
    intents=intents,
    activity=discord.Activity(
        type=discord.ActivityType.watching, name="you through a window"
        ),
    owner_id=355971553500069889
)

@bot.event
async def on_ready():
    print(f"running as {bot.user}!")

@bot.command(
    name="hi"
)
async def hi(ctx):
    return await ctx.channel.send(f"gaming with {ctx.author}")

bot.run(os.getenv("TOKEN"))