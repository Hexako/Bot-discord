import discord
from discord.ext import commands
import json
scoreboard = {}
def setup(bot):
    with open('scoreboard.json', 'r') as f:
        scoreboard = json.load(f)

    @bot.command()
    async def getScore(ctx):
        sorted_scoreboard = dict(sorted(scoreboard.items(), key=lambda item: item[1], reverse=True))
        await ctx.send(sorted_scoreboard)

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def addUser(ctx, *, text : str = "Je te spam"):
        scoreboard[text] = 0
        with open('scoreboard.json', 'w') as f:
            json.dump(scoreboard, f, indent=2)
        await ctx.send(f"{text} a été ajouté au scoreboard")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def addPoint(ctx, text : str = "user",score : int = 1):
        if text in scoreboard:
            scoreboard[text] += score
            with open('scoreboard.json', 'w') as f:
                json.dump(scoreboard, f, indent=2)
            await ctx.send(f"{text} a gagné {score} points")
        else:
            await ctx.send(f"{text} n'existe pas dans le scoreboard")