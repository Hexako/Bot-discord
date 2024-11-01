import discord
from discord.ext import commands
import random
def setup(bot):
    @bot.command()
    async def hi(ctx):
        await ctx.send("Hi !")

    @bot.command()
    async def occupation(ctx):
        await ctx.send("Tout sauf LoL")

    # !say -> fait parler le bot (il dit le message et supprime le tient)
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def say(ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")