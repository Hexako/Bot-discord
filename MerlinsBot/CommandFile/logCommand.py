import discord
from discord.ext import commands
import time

def setup(bot):
    @bot.event
    async def on_message_delete(message):
        channel = bot.get_channel(1301697629197045800)
        messageUser = message.content
        if messageUser[:1] == "!":
            return
        embed = discord.Embed(
            title=f'Message supprimé de **{message.author}**',
            description=f'**{message.content}**',
            color=0xFF0000)
        embed.set_footer(text=f'{time.asctime()}')

        await channel.send(embed=embed)
