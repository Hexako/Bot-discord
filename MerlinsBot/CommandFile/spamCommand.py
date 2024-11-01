import discord
from discord.ext import commands
import time
def setup(bot):
    # !spam [nb] [user] [intervalle de temps] [texte]
    @bot.command(aliases=['harcelement'])
    @commands.has_permissions(administrator=True)
    async def spam(ctx, nb: int, member: discord.Member, temps: int = 1, *, text: str = "Je te spam"):

        try:
            await ctx.message.delete()
            for i in range(nb):
                await ctx.send(f" {member.mention} {text}")
                time.sleep(temps)

        except:
            await ctx.message.add_reaction("❌")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def spamDM(ctx, nb: int, member: discord.Member, temps: int = 1, *, text: str = "Je te spam"):

        try:
            await ctx.message.delete()
            for i in range(nb):
                await member.send(f" {member.mention} {text}")
                time.sleep(temps)
        except:
            ctx.message.add_reaction("❌")