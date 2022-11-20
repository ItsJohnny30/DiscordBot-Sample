import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="YouPrefix", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(">> Bot is Online <<")