from discord.ext import commands
import discord

class HelpOfficial(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hp(self, ctx):
        # Lista de IDs permitidas
        allowed_ids = [
            1280179641872552008,
            1089401829999267951,
            612804996966121472,
            484429946891141120,
            1282105574426808453,
            1282132539594641449
        ]

        # Verificar si el autor del mensaje tiene una ID permitida
        if ctx.author.id not in allowed_ids:
            await ctx.send("No tienes permiso para usar este comando.")
            return

        embed = discord.Embed(title="Menú de Ayuda - Crew", color=0x00ff00)
        embed.add_field(name=".start", value="Inicia el raid.", inline=False)
        embed.add_field(name=".channels", value="Elimina todos los canales y crea uno nuevo.", inline=False)
        embed.add_field(name=".admin", value="Genera un rol con permisos de administración.", inline=False)
        embed.add_field(name=".admin_in <ID>", value="Da administrador al rol @everyone en un servidor por ID.", inline=False)
        embed.add_field(name=".banall", value="Banea a todos en el servidor.", inline=False)
        embed.add_field(name=".data", value="Saca datos del servidor en específico.", inline=False)
        embed.add_field(name=".invite <ID>", value="Saca la invitación del servidor por su ID.", inline=False)
        embed.add_field(name=".invite-force <ID>", value="Forzar sacar una invitación del servidor por su ID.", inline=False)
        embed.add_field(name=".join", value="Envía el link para invitar el bot al servidor.", inline=False)
        embed.add_field(name=".leave <ID>", value="Saca el bot de un servidor usando su ID.", inline=False)
        embed.add_field(name=".md", value="Manda mensajes directos a todos los usuarios.", inline=False)
        embed.add_field(name=".servers", value="Mapea todos los servidores donde está el bot.", inline=False)
        embed.add_field(name=".rest", value="Reinicia el bot.", inline=False)
        embed.add_field(name=".rol", value="Crea 50 roles abusivos en el servidor.", inline=False)
        embed.add_field(name=".stats", value="Mira tus estadísticas actuales.", inline=False)
        embed.add_field(name=".top", value="Top de los récords realizados por usuarios.", inline=False)
        embed.add_field(name=".unban <server_id>", value="Desbanea a miembros de Crew del servidor especificado.", inline=False)
        embed.add_field(name=".hp", value="Muestra este menú de ayuda.", inline=False)

        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(HelpOfficial(bot))
