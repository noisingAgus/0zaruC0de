from discord.ext import commands
import discord

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx, server_id: int):
        guild = self.bot.get_guild(server_id)
        
        if not guild:
            await ctx.send("No se encontró el servidor con ese ID. 😥")
            return
        
        # Intentar crear una invitación
        try:
            # Intentar crear una invitación en el primer canal de texto disponible
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).create_instant_invite:
                    invite = await channel.create_invite(max_age=300, max_uses=1)  # Invito válido por 5 minutos
                    await ctx.send(f"Invitación para el servidor **{guild.name}**: {invite}")
                    return
            
            await ctx.send("No tengo permisos para crear una invitación en ningún canal de texto. 😢")
        
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para crear una invitación. 🚫")
        except discord.HTTPException:
            await ctx.send("Hubo un error al intentar crear la invitación. 😞")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Invite(bot))
