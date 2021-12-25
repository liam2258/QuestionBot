import os
import discord
import random
from Immortal import Immortal

# This stores an encrypted version of the Discord bot's token
my_secret = os.environ['Token']

# Connects the program to Discord
client = discord.Client()


# Send feed back that the bot successfully logged into discord
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
# Returns if the bot ever sends a command to itself
async def on_message(message):
    if message.author == client.user:
        return

    # When the following commands are entered in a discord
    # server that the bot inhabits, it will send a random response to that server
    # from the designated txt file
    if message.content.startswith('?Questions?'):
        await message.channel.send('''
Type \"?Ask a question\" for random questions!
Type \"?Ask a gamer question\" for gaming questions!
Type \"?Ask a weeb question\" for otaku questions!
    ''')

    if message.content.startswith('?Ask a question'):
        await message.channel.send(random.choice(list(open('RandomQuestions.txt'))))

    if message.content.startswith('?Ask a gamer question'):
        await message.channel.send(random.choice(list(open('GamerQuestions.txt'))))

    if message.content.startswith('?Ask a weeb question'):
        await message.channel.send(random.choice(list(open('WeebQuestions.txt'))))


Immortal()
client.run(my_secret)