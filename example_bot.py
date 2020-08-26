import discord



TOKEN='NzQ4MDM2MDkwNjk4NTMwODQ2.X0Xk5Q.nINaSjjrjKXr3Yrqw7rtIwggxJw'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('bitch'):
        await message.channel.send('Hello bitch, cussing is bad 4 u')
    if message.content.startswith('pepehands'):
        await message.channel.send('pepehands lmao!')

client.run(TOKEN)
