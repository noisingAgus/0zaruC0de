from discord.ext import commands
import discord
from datetime import datetime

class Data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def data(self, ctx, server_id: int):
        guild = self.bot.get_guild(server_id)
        
        if not guild:
            await ctx.send("No se encontró el servidor con ese ID. 😥")
            return
        
        # Recopilar información del servidor
        embed = discord.Embed(title=f"Datos del Servidor: {guild.name}", color=0x00ff00)
        embed.add_field(name="Nombre", value=guild.name, inline=False)
        embed.add_field(name="ID", value=guild.id, inline=False)
        embed.add_field(name="Fecha de Creación", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Miembros Totales", value=guild.member_count, inline=False)
        embed.add_field(name="Canales Totales", value=len(guild.channels), inline=False)
        embed.add_field(name="Roles Totales", value=len(guild.roles), inline=False)
        embed.add_field(name="Propietario", value=guild.owner.mention, inline=False)
        embed.add_field(name="ID del Propietario", value=guild.owner_id, inline=False)
        embed.add_field(name="Región", value=guild.preferred_locale or "Desconocido", inline=False)
        embed.add_field(name="Nivel de Boost", value=guild.premium_tier, inline=False)
        embed.add_field(name="Boosters", value=len(guild.premium_subscribers), inline=False)
        embed.add_field(name="Canales de Texto", value=len(guild.text_channels), inline=False)
        embed.add_field(name="Canales de Voz", value=len(guild.voice_channels), inline=False)
        embed.add_field(name="Categorías", value=len(guild.categories), inline=False)
        embed.add_field(name="Emoji Personalizados", value=len(guild.emojis), inline=False)
        embed.add_field(name="Número de Stickers", value=len(guild.stickers), inline=False)
        embed.add_field(name="Seguridad del Servidor", value=str(guild.verification_level), inline=False)
        embed.add_field(name="Número de Invitaciones", value=len(await guild.invites()), inline=False)
        embed.add_field(name="Afk Timeout (en segundos)", value=guild.afk_timeout, inline=False)
        
        # Agregar el logo del servidor
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        # Agregar el banner del servidor (si existe)
        if guild.banner:
            embed.set_image(url=guild.banner.url)

        # Enviar el embed con los datos del servidor
        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Data(bot))
