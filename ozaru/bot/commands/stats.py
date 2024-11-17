from discord.ext import commands
import discord

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        embed = discord.Embed(title="Estadísticas del Bot", color=0x00ff00)
        
        # Agregar información sobre el bot
        embed.add_field(name="Nombre del Bot", value=self.bot.user.name, inline=False)
        embed.add_field(name="ID del Bot", value=self.bot.user.id, inline=False)
        embed.add_field(name="Número de Servidores", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Número de Usuarios", value=sum(g.member_count for g in self.bot.guilds), inline=False)
        embed.add_field(name="Versión de Discord.py", value=discord.__version__, inline=False)
        
        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Stats(bot))
