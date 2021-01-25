# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv
from minesweeper import Minesweeper

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def minesweeper(ctx):
    mine = Minesweeper()
    mine.new_game(8, 8, 10)

    await ctx.send(mine.print_to_discord())

bot.run(TOKEN)
