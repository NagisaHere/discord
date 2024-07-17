import discord
from discord.ext import commands
from key import get_key
from constants import *
from register_commands import register_commands
# from network import start_network


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    reboot = client.get_channel(GUILD_CHANNEL)
    await reboot.send("I have rebooted!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == "__main__":
    register_commands()
    client.run(get_key())
    # start_network()
