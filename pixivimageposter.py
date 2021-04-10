import glob, os, random, discord
from discord.ext import commands

help_command = commands.DefaultHelpCommand(no_category="Commands")
client = commands.Bot(command_prefix = '!!',help_command = help_command)

@client.event
async def on_ready():
    print("Ready!")

@client.command(help = "Posts a random image from my pixiv bookmarks")
async def pixiv(ctx):
    files = glob.glob("*.png")
    files.extend(glob.glob("*.jpg"))
    files.extend(glob.glob("*.gif"))
    file = random.choice(files)
    '''
    filenames are the default to pixivutil2, being
    "(id)_p(imgnumber) - (title).(ext)"

    link1 takes "file" and splits it with the character "_", giving you the id and the rest of the file

    link2 takes the rest of the file and splits it with a space, giving you the image number and other stuff we don't need
    it then removes "p" which just gets in the way, converts it to an integer, and adds 1 to it because pixivutil2 uses an initial zero in numbering
    '''
    link1 = file.split("_", 1)[0]
    link2 = int(file.split("_", 1)[1].split(" ", 1)[0].replace('p', ''))+1
    await ctx.send("https://pixiv.net/member_illust.php?mode=medium&illust_id=" + link1 + ", Image " + str(link2),file = discord.File(file))

client.run("token")
