import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    breaking_bad_quotes = [
        'I am the one who knocks!',
        'He can\'t keep getting away with it!',
        (
            'Say my name.'
        ),
    ]

    spongebob_quotes = [
        'HAHAHA HAHAHA it\s a giraffe!',
        'I don\'t need it, I don\'t need it, I don\'t need it ... I NEEEEED IT!!!',
        'Did you smell it? That smell. A kind of smelly smell. The smelly smell that smells...smelly.',
        'The inner machinations of my mind are an enigma.',
    ]

    if message.content == 'The good stuff':
        #response = random.choice(breaking_bad_quotes)
        response = random.choice(spongebob_quotes)
        await message.channel.send(response)

client.run(TOKEN)
