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
    await bot.change_presence(game=discord.Game(name= str(len(bot.servers)) + " servers", type=3))
    print('Ready :D') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'Pong! Im online!')
        
        
@client.event
async def on_message(message):
    if message.content.startswith('-react'):
        msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')
        res = await client.wait_for_reaction(['👍', '👎'], message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
        
client.run('NDg2NDg1MzAxMzEzNjY3MDgy.DqId0w.rC5MpzcTSm9gZX42AxIxujHI8HA')
