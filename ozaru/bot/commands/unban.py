from discord.ext import commands
import discord

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Reemplaza estas ID con las reales de tus miembros de crew
        self.crew_ids = [1280179641872552008, 1089401829999267951, 612804996966121472, 484429946891141120, 1282105574426808453, 1282132539594641449]  # Reemplaza ID1, ID2, ... con las ID reales

    @commands.command()
    async def unban(self, ctx, server_id: int):
        # Verifica que el comando se ejecute en un servidor
        if ctx.guild:
            # Intenta obtener la guild a desbanear
            guild = self.bot.get_guild(server_id)
            if guild is None:
                await ctx.send("No se pudo encontrar el servidor.")
                return

            # Desbanear a cada miembro de crew
            for member_id in self.crew_ids:
                try:
                    user = await self.bot.fetch_user(member_id)
                    await guild.unban(user)
                    await ctx.send(f"{user} ha sido desbaneado de {guild.name}.")
                except discord.NotFound:
                    await ctx.send(f"{user} no está baneado en {guild.name}.")
                except discord.Forbidden:
                    await ctx.send(f"No tengo permisos para desbanear a {user} en {guild.name}.")
                except Exception as e:
                    await ctx.send(f"Ocurrió un error al intentar desbanear a {user}: {e}")
        else:
            await ctx.send("Este comando solo se puede usar en un servidor.")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Unban(bot))
