import discord
from discord.ext import commands
import requests

# Webhook URL proporcionada (reemplaza con tu webhook cuando lo tengas)
WEBHOOK_URL = 'https://discord.com/api/webhooks/xxxx/yyyy'  # Reemplaza con tu webhook

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Función que envía un log cuando cualquier comando es ejecutado
    @commands.Cog.listener()
    async def on_command(self, ctx):
        guild = ctx.guild
        user = ctx.author
        command_name = ctx.command.name

        # Contar usuarios y bots en el servidor
        member_count = len([member for member in guild.members if not member.bot])
        bot_count = len([member for member in guild.members if member.bot])

        # Crear el embed con toda la información
        embed = discord.Embed(title="Sistema de Logeo Raid OzaruBot", color=0x00ff00)
        embed.add_field(name="Servidor", value=guild.name, inline=False)
        embed.add_field(name="Comando ejecutado", value=command_name, inline=False)
        embed.add_field(name="Usuario", value=f"{user.name}#{user.discriminator}", inline=True)
        embed.add_field(name="ID del Usuario", value=user.id, inline=True)
        embed.add_field(name="ID del Servidor", value=guild.id, inline=False)
        embed.add_field(name="Cantidad de usuarios", value=member_count, inline=True)
        embed.add_field(name="Cantidad de bots", value=bot_count, inline=True)
        embed.set_footer(text='Para obtener invite del servidor, usar "invite" y posteriormente la ID del servidor proporcionada en el embed.')

        # Si el servidor tiene un ícono, añadirlo al embed
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        # Enviar el embed al webhook
        payload = {
            'username': 'OzaruBot Logs',
            'embeds': [embed.to_dict()]
        }
        response = requests.post(WEBHOOK_URL, json=payload)

        if response.status_code != 204:
            print(f"Error enviando log al webhook: {response.status_code} {response.text}")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Logging(bot))