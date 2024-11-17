from discord.ext import commands
import discord

class Servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def servers(self, ctx):
        # Obtener todos los servidores donde está el bot
        guilds = self.bot.guilds
        
        # Crear un embed para mostrar la información
        embed = discord.Embed(title="Servidores donde está el bot", color=0x00ff00)
        
        for guild in guilds:
            embed.add_field(name=guild.name, value=f"ID: {guild.id} | Miembros: {guild.member_count}", inline=False)

        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Servers(bot))
