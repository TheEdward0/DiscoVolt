import discord, os, alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(command_prefix='$', self_bot=True)


# name = for your status and url = for your twitch link
@client.event
async def on_connect():
    await client.change_presence(activity=discord.Streaming(
        name="Hey Im Edward",
        url="https://www.youtube.com/watch?v=3qJWEFeelLE"))


class color:
    Purple = '\033[95m'
    RED = '\033[91m'
    wormy = '\033[93m'


print(color.Purple + """

░██████╗██╗░░██╗░█████╗░████████╗███████╗██████╗░██████╗░██╗███████╗
██╔════╝██║░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║██╔════╝
╚█████╗░███████║██║░░██║░░░██║░░░█████╗░░██║░░██║██║░░██║██║█████╗░░
░╚═══██╗██╔══██║██║░░██║░░░██║░░░██╔══╝░░██║░░██║██║░░██║██║██╔══╝░░
██████╔╝██║░░██║╚█████╔╝░░░██║░░░███████╗██████╔╝██████╔╝██║███████╗
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░╚═════╝░╚═╝╚══════╝
""")


def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)


printLow(color.Purple + """
Discord : discord.gg/hTP2DaMCnD
Youtube : youtube.com/@ShotEddie


""")

alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
