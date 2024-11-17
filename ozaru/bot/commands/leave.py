from discord.ext import commands

class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leave(self, ctx, guild_id: int):
        # Intenta obtener el servidor con el ID proporcionado
        guild = self.bot.get_guild(guild_id)
        if guild:
            # Si el bot está en el servidor, se desconectará
            await guild.leave()
            await ctx.send(f'El bot ha salido del servidor: {guild.name}')
        else:
            await ctx.send('El bot no está en el servidor con ese ID.')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Leave(bot))
