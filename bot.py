import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# This can be changed according to your bot's permission usage requirements
intent = discord.Intents.all()

# The command prefix can be changed here as well. If you want to use the default
# help message simply delete the help_command argument along with the help method
bot = commands.Bot(command_prefix="!", intents=intent, help_command=None)

# Load all cogs in this method here#
# If you would like to implement your own cogs without
# the botbuilder's built-in feature, use the line below
# to import the cog. Replace 'extension' with your filename
# await bot.load_extension("extension")
@bot.event
async def on_ready():
    print("Cogs loaded!")

# Test the bot's connection
@bot.command()
async def ping(ctx):
    await ctx.channel.send("Pong!")

# Custom help message can be created here
@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description = "These are the commands that you can use for this bot", colour = discord.Colour.teal())
    MyEmbed.set_thumbnail(url = "https://images-eds-ssl.xboxlive.com/image?url=4rt9.lXDC4H_93laV1_eHHFT949fUipzkiFOBH3fAiZZUCdYojwUyX2aTonS1aIwMrx6NUIsHfUHSLzjGJFxxsG72wAo9EWJR4yQWyJJaDb6rYcBtJvTvH3UoAS4JFNDaxGhmKNaMwgElLURlRFeVkLCjkfnXmWtINWZIrPGYq0-&format=source&h=307")
    MyEmbed.add_field(name = "!ping", value = "This command replies with Pong! when you write !ping", inline = False)
    await ctx.send(embed = MyEmbed)

# Used to load a cog mid-production so you do not have to restart the bot
@bot.command()
async def load(ctx, *,name):
    await bot.load_extension(name)

# Used to unload a cog mid-production so you do not have to restart the bot
@bot.command()
async def unload(ctx, *,name):
    await bot.unload_extension(name)
                
# Used to reload a cog mid-production so you do not have to restart the bot
@bot.command()
async def reload(ctx, *,name):
    await bot.reload_extension(name)

bot.run(TOKEN)