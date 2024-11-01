
def setup(bot):
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