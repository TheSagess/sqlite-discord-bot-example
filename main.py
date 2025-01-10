import logging
import os
import discord
import sqlite3
import datetime
import sys
import io
import textwrap
import traceback
import aiohttp
import inspect
import asyncio
import botsetup
from discord.ext.commands import ExtensionNotFound, ExtensionFailed
from datetime import datetime
from config import config

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()  # Sets the default bot intents
intents.guilds = True
intents.members = True  # Allows the bot to see members in a guild
intents.message_content = True  # Allows the bot to see message content


TOKEN = os.getenv("token")  # Sets the bot's token
COMMAND_PREFIX = "?"  # Sets the bots command prefix for non app commands
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)  # Defines bot

async def load_cogs(bot):
    cogs = [config]  # Ensure these are properly imported
    for cog in cogs:
        if not bot.get_cog(cog.__name__):
            try:
                await bot.load_extension(cog.__name__)
                print(f"Successfully loaded cog: {cog.__name__}")
            except ExtensionNotFound:
                print(f"Cog {cog.__name__} not found. Please check the module name and path.")
            except ExtensionFailed as e:
                print(f"Cog {cog.__name__} failed to load: {e}")
            except Exception as e:
                print(f"Unexpected error occurred while loading cog {cog.__name__}: {e}")



bot.run(TOKEN)
