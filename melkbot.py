import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready :D') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'pooooooooooooooooooooooooooooooooooong.')
client.run('NDg2NDg1MzAxMzEzNjY3MDgy.DqId0w.rC5MpzcTSm9gZX42AxIxujHI8HA')
