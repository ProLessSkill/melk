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
    await client.change_presence(game=Game(name='with Milk :>'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'Pong! Im online, serving fresh Melk!')
    if message.content == '-credits':
        await client.send_message(message.channel,'**Contributors:** `ProLessSkill#7393 - Owner`')
client.run('NDg2NDg1MzAxMzEzNjY3MDgy.DqJMXg.IZ4bShqdoi7IbMK9DNlrk9RqN2o')
