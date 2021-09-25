import os
from dotenv import load_dotenv

import discord

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f"running as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!hi"):
        await message.channel.send(f"gaming with {message.author}")

client.run(os.getenv("TOKEN"))