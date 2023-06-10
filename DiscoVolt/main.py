import discord, os, alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(command_prefix='!', self_bot=True)


# name = for your status and url = for your twitch link
@client.event
async def on_connect():
    await client.change_presence(activity=discord.Streaming(
        name="Hey Im Edward",
        url="https://www.youtube.com/watch?v=3qJWEFeelLE"))


alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
