from discord.ext import commands
import discord

class InviteForce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite_force(self, ctx, server_id: int):
        guild = self.bot.get_guild(server_id)
        
        if not guild:
            await ctx.send("No se encontró el servidor con ese ID. 😥")
            return
        
        # Intentar crear una invitación sin restricciones de permisos
        try:
            # Forzar la creación de la invitación en el primer canal de texto
            for channel in guild.text_channels:
                invite = await channel.create_invite(max_age=300, max_uses=1)  # Invito válido por 5 minutos
                await ctx.send(f"Invitación forzada para el servidor **{guild.name}**: {invite}")
                return
            
            await ctx.send("No se pudo crear una invitación en ningún canal. 😢")
        
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para crear la invitación. 🚫")
        except discord.HTTPException:
            await ctx.send("Hubo un error al intentar crear la invitación. 😞")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(InviteForce(bot))
