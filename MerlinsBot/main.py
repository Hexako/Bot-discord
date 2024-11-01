import discord
from discord.ext import commands
from TOKEN import token
import random
import time
from MerlinsBot.CommandFile import pingCommand,logCommand,spamCommand,tournamentCommand,baseCommand,jokeCommand,emojiCommand



# intents : en rapport avec les permissions
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents=intents)

bot.remove_command("help")
pingCommand.setup(bot)
logCommand.setup(bot)
spamCommand.setup(bot)
tournamentCommand.setup(bot)
baseCommand.setup(bot)
jokeCommand.setup(bot)
emojiCommand.setup(bot)

@bot.event
async def on_ready():
    print(f"Bot prêt ! |{bot.user.name}|")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Soulager la peine de Yann'))

print(f'Lancement du bot...')
bot.run(token)