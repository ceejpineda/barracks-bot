import os
import discord
import requests
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI
import asyncio

from discord.ext import commands



cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="c3_dev"
)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.load_extension('cogs.fun')
    await bot.load_extension('cogs.guild')
    await bot.load_extension('cogs.lands')

bot.run(TOKEN)
