import discord
from discord.ext import commands
import random

def setup(bot):
    # !team [nb de team] -> Faire s'affronter nb équipes contre. ex : équipe 6 vs équipe 3, etc.
    @bot.command()
    async def team(ctx, nb: int):
        equipe = [i for i in range(1, nb + 1)]
        if nb % 2 != 0:
            impaire = random.choice(equipe)
            equipe.remove(impaire)
        for i in range(nb // 2):
            x = random.choice(equipe)
            equipe.remove(x)
            y = random.choice(equipe)
            equipe.remove(y)
            await ctx.send(f'Équipe {x} vs Équipe {y}')
        if nb % 2 != 0:
            await ctx.send(f'Equipe restante : Equipe {impaire}')