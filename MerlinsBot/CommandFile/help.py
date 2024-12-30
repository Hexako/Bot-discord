import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View, Button

# Pour chemins windows/linux
import os.path

def setup(bot):
    @bot.tree.command(name="help", description="Commande d'aide")
    @app_commands.describe()
    async def help(interaction: discord.Interaction):

        with open(f"{os.path.normpath(os.path.dirname(os.path.dirname(__file__)))}/help.txt", "r", encoding='utf-8') as f:

            commande, commandes = [], []
            det = []
            com = 0

            for lines in f:
                line = lines.replace("\n", "")
                if line.startswith("-"):
                    com += 1
                if com in range(1, 6):
                    if line.startswith("-"):
                        line = line.replace("-", "")
                    commande.append(line)
                    com += 1
                elif com == 6:
                    if list(line)[-1] != '/':
                        det.append(lines)
                    else:
                        det.append(line[:-1])
                        commande.append(''.join(det))
                        det = []
                        com = 0
                        commandes.append(commande)
                        commande = []

        def message_base():

            mess = '\n'.join([f'`{commandes[i][0]}` - {commandes[i][3]}' for i in range(len(commandes))])

            embed = discord.Embed(
                title="**Liste des commandes**\n\n",
                description=mess,
                color=0x00FA1D
            )

            return embed

        def message_det(num):

            if commandes[num-1][2] == "*":
                alias = ""
            else:
                alias = f"Aliases : `{'` `'.join(commandes[num-1][2].split(','))}`\n"

            type = commandes[num-1][1]
            if type == ("u"):
                type = "Utilitaire"
            elif type == ("a"):
                type = "Administration"
            elif type == ("f"):
                type = "Fun"

            embed = discord.Embed(
                title=f"Détails de la commande : `{commandes[num-1][0]}`\n\n",
                description=f"Catégorie : {type}\n" + alias + f"\n__Description détaillée :__\n{commandes[num-1][5]}\n\n" + f"[Exemple d'utilisation de la commande]({commandes[num-1][4]})",
                color=0x00FA1D
            )

            return embed


        nom_commandes = [commande[0] for commande in commandes]

        options = (
                [discord.SelectOption(label="Retour", value="0")] +
                [discord.SelectOption(label=f"{nom_commandes[i]}", value=str(i+1)) for i in range(len(nom_commandes))]
        )

        select = Select(placeholder="Détails sur les commandes", min_values=1, max_values=1, options=options)

        async def select_callback(interaction: discord.Interaction):

            # Num commande choisie
            num_com = int(select.values[0])

            if num_com == 0:
                await interaction.response.edit_message(embed=message_base())

            else:

                await interaction.response.edit_message(embed=message_det(num_com), view=view)

        select.callback = select_callback
        view = View()
        view.add_item(select)

        # Envoie du message avec le menu déroulant
        await interaction.response.send_message(embed=message_base(), view=view)