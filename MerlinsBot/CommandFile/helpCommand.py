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

            mess = '\n'.join([f'`{commandes[i][0]}` - {commandes[i][3]}' for i in range(len(commandes)) if commandes[i][1] != "a"])

            # Pour le cas type = "a"
            if admin:
                b = '\n'.join([f'`{commandes[i][0]}` - {commandes[i][3]}' for i in range(len(commandes)) if commandes[i][1] == "a"])
                a = f"\n\n**__Admin__**\n{b}"
            else: a = ""

            embed = discord.Embed(
                title="**Liste des commandes**\n\n",
                description=mess + a,
                color=0x00FA1D
            )

            return embed

        def message_det(num, commandes):

            temp = [i for i in commandes if i[1] != "a"]
            temp += [i for i in commandes if i[1] == "a"]
            commandes = temp

            # Pour l'aliases
            if commandes[num-1][2] == "*":
                alias = ""
            else:
                alias = f"Aliases : `{'` `'.join(commandes[num-1][2].split(','))}`\n"

            # Pour la catégorie
            type = commandes[num-1][1]
            if type == ("u"):
                type = "Utilitaire"
            elif type == ("a"):
                type = "Administration"
            elif type == ("f"):
                type = "Fun"


            embed = discord.Embed(
                title=f"Détails de la commande : `{commandes[num-1][0]}`\n\n",
                description=f"Catégorie : {type}\n" +
                            alias + f"\n__Description détaillée :__\n{commandes[num-1][5]}\n\n" +
                            f"[Exemple d'utilisation de la commande]({commandes[num-1][4]})",
                color=0x00FA1D
            )

            return embed


        nom_commandes = [commande[0] for commande in commandes if commande[1] != "a"]

        #Celui qui clique
        user = interaction.user
        # Celui qui clique est dans le serveur ? (et donc pas en MP)
        if interaction.guild:
            # Celui qui clique a t'il les perms admin ?
            admin = user.guild_permissions.administrator
            if admin:
                nom_commandes += [commande[0] for commande in commandes if commande[1] == "a"]
        else: admin = False

        # Ce qui sera affiché dans le menu déroulant
        options = (
                [discord.SelectOption(label="Retour", value="0")] +
                [discord.SelectOption(label=f"{nom_commandes[i]}", value=str(i+1)) for i in range(len(nom_commandes))]
        )

        select = Select(placeholder="Détails sur les commandes", min_values=1, max_values=1, options=options)

        async def select_callback(interaction: discord.Interaction):

            # Num commande choisie
            num_com = int(select.values[0])

            # Vérif si c'est la même personne qui à fait la commande et qui à cliqué
            if user != interaction.user:
                await interaction.response.send_message("Il faut être à l'origine de la commande pour pouvoir interagir", ephemeral=True)
                return

            if num_com == 0:
                await interaction.response.edit_message(embed=message_base())

            else: await interaction.response.edit_message(embed=message_det(num_com, commandes), view=view)

        select.callback = select_callback
        view = View()
        view.add_item(select)

        # Envoie du message avec le menu déroulant
        await interaction.response.send_message(embed=message_base(), view=view)