import discord
from discord.ext import commands
from TOKEN import token
import random
import time


# intents : en rapport avec les permissions
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)

bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Bot prêt ! |{bot.user.name}|")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Soulager la peine de Yann'))
@bot.command()
async def hi(ctx):
    await ctx.send("Hi !")
@bot.command()
async def occupation(ctx):
    await ctx.send("Tout sauf LoL")
# !team [nb de team] -> Faire s'affronter nb équipes contre. ex : équipe 6 vs équipe 3, etc.
@bot.command()
async def team(ctx, nb: int):
    equipe = [i for i in range(1, nb+1)]
    if nb%2 != 0:
        impaire = random.choice(equipe)
        equipe.remove(impaire)
    for i in range(nb//2):
        x= random.choice(equipe)
        equipe.remove(x)
        y = random.choice(equipe)
        equipe.remove(y)
        await ctx.send(f'Équipe {x} vs Équipe {y}')
    if nb%2 != 0:
        await ctx.send(f'Equipe restante : Equipe {impaire}')




# !e [message] -> envoi réactions du message sur mess répondu
@bot.command(aliases=['e'])
async def emoji(ctx, *, mess):
    if len(mess) == len(set(mess)) and all(c.isalpha() for c in mess):
        await ctx.message.delete()
        id = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        emoji_ids = {chr(i): chr(127462 + i - ord('a')) for i in range(ord('a'), ord('z') + 1)}

        for char in mess.lower():
            emoji_id = emoji_ids.get(char)
            if emoji_id:
                await id.add_reaction(emoji_id)
    else:
        await ctx.message.add_reaction("❌")

# !spam [nb] [user] [intervalle de temps] [texte]
@bot.command(aliases=['harcelement'])
async def spam(ctx, nb: int, member: discord.Member , temps: int = 1, *, text: str = "Je te spam"):

    try:
        await ctx.message.delete()
        if ctx.author.id == 431181653780725791:
            for i in range(nb):
                await ctx.send(f" {member.mention} {text}")
                time.sleep(temps)
        else:
            if nb <= 15 and member.id != 431181653780725791 and temps <= 5:
                for i in range(nb):
                    await ctx.send(f" {member.mention} {text}")
                    time.sleep(temps)
            else: await ctx.send("Spammer, c'est mal. Revoie les valeurs que tu as mit à la baisse. Faut pas abuser non plus.")

    except: await ctx.message.add_reaction("❌")


@bot.command()
async def spamDM(ctx, nb: int, member: discord.Member , temps: int = 1, *, text: str = "Je te spam"):

    try:
        await ctx.message.delete()
        if ctx.author.id == 431181653780725791:
            for i in range(nb):
                await member.send(f" {member.mention} {text}")
                time.sleep(temps)
        else: await ctx.send("Tu n'es pas assez puissant pour utiliser cette commande. Et de toute façon : **Spammer, c'est mal.**") # pareil que au dessus mais spam en DM

    except: ctx.message.add_reaction("❌")

print(f'Lancement du bot...')
bot.run(token)