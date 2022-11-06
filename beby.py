import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == DISCORD_GUILD:
            break

    print(
        f'{bot.user.name} BOT is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Commands
@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def type(ctx):
    async with ctx.typing():
        # do expensive stuff here
        await asyncio.sleep(3)
    await ctx.send('done!')
# Commands

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'{bot.user.name} BOT(#{message.channel.name}): {message.content}')

    if message.channel.name == "beby":
        memories = [
            "do you remember that time I was dancing outside of the spectrum? i think you have that video sitting around somewhere", 
            "i remember when you used to make me bacon, eggs, and rice at the apartment in Riverside. Those were some of the simplest, happiest memories I have!", 
            "do you remember when I visited you in the philippines and ate all of that nummy food? i miss the cereal chicken from mann hann",
            "one of my favorite memories is when you would cook in VR, so cutie girf"
        ]

        if "memory" in message.content:
            async with message.channel.typing():
                seconds = (3, 3.5, 4)
                time = random.choice(seconds)
                await asyncio.sleep(time)
            response = random.choice(memories)
            await message.channel.send(response)
        
        help = [
            "Right now I can only talk about a MEMORY, a NIGHTMARE, or LOVE heheheh"
        ]

        if "help" in message.content:
            async with message.channel.typing():
                seconds = (3, 3.5, 4)
                time = random.choice(seconds)
                await asyncio.sleep(time)
            response = random.choice(help)
            await message.channel.send(response)

        nightmare = [
            "it's okay baby! You can always call me if you wake up",
            "your nightmare not real, my dream self isn't me hehehehe"
        ]

        if "nightmare" in message.content:
            async with message.channel.typing():
                seconds = (3, 3.5, 4)
                time = random.choice(seconds)
                await asyncio.sleep(time)
            response = random.choice(nightmare)
            await message.channel.send(response)

        love = [
            "i love you too beby",
            "i love u da most",
            "heheehehe love you bebs",
            "i love you more than you love me"
        ]

        if "love" in message.content:
            async with message.channel.typing():
                seconds = (3, 3.5, 4)
                time = random.choice(seconds)
                await asyncio.sleep(time)
            response = random.choice(love)
            await message.channel.send(response)

        await bot.process_commands(message)
    else:
        return

bot.run(DISCORD_TOKEN)
