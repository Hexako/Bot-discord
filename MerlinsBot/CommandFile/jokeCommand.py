from blagues_api import BlaguesAPI, BlagueType
blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDMxMTgxNjUzNzgwNzI1NzkxIiwibGltaXQiOjEwMCwia2V5IjoiTVRQbEJORFdGNXVYTHRFdjAwUFR1MjNXRHJNY1pra3RqcEEwWUJVRGIxekxmSmpzYUgiLCJjcmVhdGVkX2F0IjoiMjAyMy0xMC0xNlQyMDowMDowNyswMDowMCIsImlhdCI6MTY5NzQ4NjQwN30.99n9pQSqkRjmUvf-aPsRltjW2AbPMYRAgvuCIILoVTk")

def setup(bot):
    # !blague -> Fait des blagues quoi...
    @bot.command(aliases=['b'])
    async def blague(ctx):
        blague = await blagues.random()
        await ctx.send(f"*type de blague : {blague.type}*\n{blague.joke}\n||{blague.answer}||")

    @bot.command(aliases=['bdev'])
    async def blaguedev(ctx):
        blague = await blagues.random_categorized(BlagueType.DEV)
        await ctx.send(f"*type de blague : {blague.type}*\n{blague.joke}\n||{blague.answer}||")