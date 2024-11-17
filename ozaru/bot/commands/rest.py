import os
import sys
import discord
from discord.ext import commands

class BotControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rest(self, ctx):
        await ctx.send("Reiniciando el bot...")
        await self.bot.close()  # Cierra el bot

        # Aquí puedes reiniciar el bot; esto depende de cómo lo estés ejecutando.
        # Si estás usando un script de inicio, podrías reiniciar el script desde ahí.
        os.execv(sys.executable, ['python'] + sys.argv)  # Reinicia el bot

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(BotControl(bot))
