from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        # ID del bot (reemplaza con el ID de tu bot)
        bot_id = self.bot.user.id
        
        # URL de invitación (ajusta los permisos como sea necesario)
        invite_link = f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot"
        
        await ctx.send(f"Aquí tienes la invitación para añadir el bot a tu servidor: {invite_link}")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Join(bot))
