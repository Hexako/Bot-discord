from blagues_api import BlaguesAPI, BlagueType
from TOKEN import blagues

blagues = BlaguesAPI(blagues)

def setup(bot):
    # !blague -> Fait des blagues quoi...
    @bot.command(aliases=['b'])
    async def blague(ctx, *, txt):

        if txt == "dev":
            blague = await blagues.random_categorized(BlagueType.DEV)
        else:
            blague = await blagues.random()

        await ctx.send(f"*type de blague : {blague.type}*\n{blague.joke}\n||{blague.answer}||")