import discord
from discord.ext import commands
from TOKEN import token
import random


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
    verif = False

    if len(mess) == len(set(mess)):

        for i in list(mess.lower()):
            if i in [chr(lettre) for lettre in range(ord('a'), ord('z') + 1)]:
                verif = True
            else:
                verif = False
                break

        if verif:
            await ctx.message.delete()
            id = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            emoji_ids = {
                'a': '🇦',
                'b': '🇧',
                'c': '🇨',
                'd': '🇩',
                'e': '🇪',
                'f': '🇫',
                'g': '🇬',
                'h': '🇭',
                'i': '🇮',
                'j': '🇯',
                'k': '🇰',
                'l': '🇱',
                'm': '🇲',
                'n': '🇳',
                'o': '🇴',
                'p': '🇵',
                'q': '🇶',
                'r': '🇷',
                's': '🇸',
                't': '🇹',
                'u': '🇺',
                'v': '🇻',
                'w': '🇼',
                'x': '🇽',
                'y': '🇾',
                'z': '🇿',
            }

            for i in list(mess.lower()):
                emoji_id = emoji_ids.get(i)
                if emoji_id:
                    await id.add_reaction(emoji_id)


        else:
            await ctx.message.add_reaction("❌")
    else:
        await ctx.message.add_reaction("❌")

print(f'Lancement du bot...')
bot.run(token)