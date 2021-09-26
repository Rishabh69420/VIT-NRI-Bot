import discord
from discord.ext import commands

class StarBoard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.pin_cache = set()
        self.pin_threshold = 1
        self.starboard_channel = "887887557919113339"

    async def on_reaction_add(self, reaction, user):
        if str(reaction) == "⭐": # and user != self.bot.user
            if reaction.message == self.pin_cache:
                if reaction.count == self.pin_threshold:
                    ctx = await self.bot.get_context()
                    self.pin_cache.remove(reaction.message)
                    ctx.self.starboard_channel.send("works lol")
            else:
                self.pin_cache.add(reaction.message)