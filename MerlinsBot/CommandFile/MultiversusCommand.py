import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View, Button

# Pour chemins windows/linux
import os.path

# DDB
import sqlite3

def setup(bot):

    def connection(ddb_name):

        chemin = os.path.normpath(f'{os.path.dirname(__file__)}/database_')

        db_exists = os.path.exists(f'{chemin}{ddb_name}.db')
        conn = sqlite3.connect(f'{chemin}{ddb_name}.db')

        # Si la ddb n'existe pas
        if not db_exists:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(id INT, team INT)""")


        conn.commit()
        return conn

    # Commande slash Multi
    # Note : la liste déroulante ne reste active que 15min si elle n'est pas actualisé.
    @bot.tree.command(name="multi", description="Crée des équipes dans MultiVersus")
    @app_commands.describe(nb_team="Nombre d'équipes")
    async def multi(interaction: discord.Interaction, nb_team: int):

        conn = connection("MultiVersus")
        cursor = conn.cursor()
        def message():

            teams = []
            for i in range(1, nb_team + 1):
                team = [row[0] for row in cursor.execute(f"SELECT id FROM user WHERE team = {i}").fetchall()]
                teams.append(f"**Équipe {i}**\n" + "\n".join(f"- <@{member}>" for member in team))

            embed = discord.Embed(
                title=f'**Équipes MultiVersus**\n',
                description='\n\n'.join(teams),
                color=0x00FA1D)

            return embed

        # Création d'un menu déroulant pour le choix d'équipe
        options = (
                [discord.SelectOption(label="Je ne veux pas d'équipe", value="0")] +
                [discord.SelectOption(label=f"Équipe {i}", value=str(i)) for i in range(1, nb_team + 1)]
        )

        select = Select(placeholder="Choisis ton équipe...", min_values=1, max_values=1, options=options)

        async def select_callback(interaction: discord.Interaction):
            # La team choisis
            selected_team = int(select.values[0])
            # Celui qui clique
            user_id = interaction.user.id
            # récup l'id de tous ceux dans la ddb
            all_id = [row[0] for row in cursor.execute("SELECT id FROM user").fetchall()]

            if user_id not in all_id:
                cursor.execute("INSERT INTO user (id, team) VALUES (?, ?)", (user_id, selected_team))
            else:
                cursor.execute("UPDATE user SET team = ? WHERE id = ?", (selected_team, user_id))

            conn.commit()
            await interaction.response.edit_message(embed=message(), view=view)

        select.callback = select_callback
        view = View()
        view.add_item(select)

        # Envoie du message avec le menu déroulant
        await interaction.response.send_message(embed=message(), view=view)