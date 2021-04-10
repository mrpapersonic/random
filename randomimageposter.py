import glob, os, random, discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!!')

@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def random(ctx):
    files = glob.glob("*.png")
    files.extend(glob.glob("*.jpg"))
    files.extend(glob.glob("*.gif"))
    file = random.choice(files)
    await ctx.send(file=discord.File(file))

client.run("PUT TOKEN HERE")