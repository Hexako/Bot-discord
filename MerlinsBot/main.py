import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View, Button
from TOKEN import token, blagues
import random
import time
import sqlite3
import os.path
from CommandFile import *




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
scoreboardCommand.setup(bot)
MultiversusCommand.setup(bot)


@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} prêt !")

    try:
        synced = await bot.tree.sync()  # Synchronise les commandes Slash
        print(f"Commandes Slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation : {e}")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Soulager la peine de Yann'))

print(f'Lancement du bot...')
bot.run(token)