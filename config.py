import discord
from discord import app_commands
from discord.ext import commands
import requests
import time

DATABASE_FILE = "database.db"

class config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()

    @app_commands.command(name="info_message_setup", description="setup the info message")
    async def setup_info_message(self, inter: discord.Interaction, message: str):
       guild_id = inter.guild_id
       channel_id = channel.id

       query = "UPDATE guilds SET info_text  = ? WHERE guild_id = ?"
       self.cursor.execute(query, (message, guild_id))
       await inter.response.send_message(f"Info Text set to {message}", ephemeral=True)
       self.conn.commit()


async def setup(bot):
    await bot.add_cog(config(bot))
