from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Lista de comandos de OzaruBot!", color=0x00ff00)
        embed.set_footer(text="DEVELOPED BY: CIRO")
        embed.set_image(url="https://media.discordapp.net/attachments/1287848627858833501/1287849936821686272/3a167c94ab96cf6d0f7c18e9c9e2b3dd.jpg?ex=66f30b38&is=66f1b9b8&hm=21c86766c7039846e321cbe792b3a397d8fd15a7570fcf3c5eca6a8ba4a78534&=&format=webp")  # Reemplaza con la URL de la imagen cuando la tengas

        # Añadir un campo para el subtítulo
        embed.description = "prefix = $"
        
        # Añadir los comandos y sus descripciones
        embed.add_field(name="start", value="Raid completo.", inline=False)
        embed.add_field(name="channels", value="Borra todos los canales y crea uno solo.", inline=False)
        # Añadir más comandos según sea necesario

        await ctx.send(embed=embed)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(Help(bot))
