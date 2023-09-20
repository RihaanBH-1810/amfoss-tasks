import os
import discord
import scraper
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command(name='livescore', help='Fetches live scores of cricket matches!')
async def livescore(ctx):
    response = scraper.scrape()
    await ctx.send(response)

@bot.command(name='generate',help='Returns the csv file')
async def generate(ctx):
    file = discord.File("scores.csv")
    await ctx.send(file = file,content = "The csv file containing the scores:")

@bot.event
async def on_command_error(ctx,error):
    await ctx.send('Wrong Command type !help for further details.')

bot.run(TOKEN)