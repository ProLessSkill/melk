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
    await client.change_presence(game=Game(name='despacito with Melk'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'Pong! Im online, playing despacito!')
    if message.content == '-credits':
        await client.send_message(message.channel,'**Contributors:** `ProLessSkill#7393 - Owner`')
    if message.content.startswith('-DidIDrinkEnoughMelk'):
        randomlist = ['no. you need to drink more!','sure i guess','you did not drink at all.','just a little bit more...',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '-quote':
        em = discord.Embed(description='Keep your friends close, but your enemies closer.')
        em.set_image(url='https://www.google.bg/search?q=nature+images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiqvbCrnYHeAhUCjywKHffxD8oQ_AUIDigB&biw=1920&bih=938#imgrc=zTqmwGzV3Q_bIM')
        await client.send_message(message.channel, embed=em)
    if message.content == '-invite':
        await client.send_message(message.channel,'Hey big bois! Im Melk, your favorite bot. Now invite me to your server to not be like a retard. Im being updated very frequently and with 24/7 uptime. Inv. Link: ')
    if message.content == '-serverping':
        await client.send_message(message.channel,'❗ Specify a Server! Eg: ```Europe | USA```')
    if message.content == '-serverping USA':
        await client.send_message(message.channel,'❌ Server is down, not responding or out of space.')
    if message.content == '-serverping Europe':
        await client.send_message(message.channel,'✔️ Server is currently online and working. Note: This is the default server!')
client.run('NDg2NDg1MzAxMzEzNjY3MDgy.DqJMXg.IZ4bShqdoi7IbMK9DNlrk9RqN2o')
