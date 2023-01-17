import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Boss just leave it to me.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello' or message.content == 'Hello':
        await message.channel.send('Hello beta')

client.run('haha')