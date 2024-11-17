from discord.ext import commands

class MD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def md(self, ctx):
        # Mensajes a enviar
        messages = ["Crew is here, fucker", "Owned-By-Crew", "discord.gg/bardo", "discord.gg/bardo"]
        members = ctx.guild.members  # Obtener todos los miembros del servidor
        
        # Enviar mensajes directos a cada miembro
        for member in members:
            if not member.bot:  # Ignorar bots
                for message in messages:  # Enviar cada mensaje individualmente
                    try:
                        await member.send(message)
                    except Exception as e:
                        print(f'No se pudo enviar mensaje a {member.name}: {e}')
        
        await ctx.send('Mensajes enviados a todos los usuarios.')

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(MD(bot))
