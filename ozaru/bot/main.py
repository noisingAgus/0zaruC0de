import discord
from discord.ext import commands

# Crear los intents y habilitar los necesarios
intents = discord.Intents.default()
intents.messages = True  # Permitir el acceso a los mensajes
intents.guilds = True    # Permitir el acceso a la información del servidor
intents.message_content = True  # Habilitar el acceso al contenido de los mensajes (necesario para comandos)

# Inicializa el bot con el prefijo $ y los intents
bot = commands.Bot(command_prefix="$", intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    # Cambiar el estado del bot cuando esté listo
    activity = discord.Streaming(
        name="Transmitiendo para 1230 servidores",
        url="https://twitch.tv/"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Bot {bot.user} está listo y con rich presence activado en modo streaming.')

@bot.event
async def setup_hook():
    # Cargar los comandos desde la carpeta 'commands'
    await bot.load_extension("commands.start")
    await bot.load_extension("commands.channels")
    await bot.load_extension("commands.help") 
    await bot.load_extension("commands.admin")
    await bot.load_extension("commands.banall")
    await bot.load_extension("commands.data")
    await bot.load_extension("commands.invite")
    await bot.load_extension("commands.invite_force")
    await bot.load_extension("commands.join")
    await bot.load_extension("commands.leave")
    await bot.load_extension("commands.md")
    await bot.load_extension("commands.servers")
    await bot.load_extension("commands.rest")
    await bot.load_extension("commands.rol")
    await bot.load_extension("commands.stats")
    await bot.load_extension("commands.top")
    await bot.load_extension("commands.unban")
    await bot.load_extension("commands.hp")
    await bot.load_extension("commands.admin_in")
    await bot.load_extension("commands.logger")
    await bot.load_extension("commands.webhook")
# Ejecutar el bot con tu token
bot.run('MTI4Nzg0NDg0ODEzMjU1ODkzMA.G8CNtO.qzd_OCwWHdLwHiD9nitLrPMsvvs6DFI0DI6Bj4')
