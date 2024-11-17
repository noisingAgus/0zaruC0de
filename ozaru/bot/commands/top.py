from discord.ext import commands
from collections import Counter
import discord

class Top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.command_usage = Counter()  # Almacena el uso de comandos por usuario

    @commands.Cog.listener()
    async def on_command(self, ctx):
        # Incrementar el contador de uso del comando para el autor
        self.command_usage[ctx.author.id] += 1

    @commands.command()
    async def top(self, ctx):
        # Obtener los 5 usuarios con más comandos ejecutados
        top_users = self.command_usage.most_common(5)

        embed = discord.Embed(title="Top de Comandos Ejecutados", color=0x00ff00)

        for user_id, count in top_users:
            user = self.bot.get_user(user_id)
            if user:  # Verificar si el usuario todavía está en Discord
                embed.add_field(name=f"{user.name}#{user.discriminator}", value=f"{count} comandos ejecutados", inline=False)

        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Top(bot))
