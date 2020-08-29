import discord



TOKEN='SOMETHING_SECRET_HAHA_IAINTJHAGINVINTOAJDSFL'

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

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '🔪':
        msg = 'I see ' + user.name + ' has reacted with a knife. You think you\'re some real slick sh*t, huh?'
        await reaction.message.channel.send(msg)
        await reaction.message.channel.send('You better watch out punk 🤏👀')

    if reaction.emoji == '🐸':
        await message.channel.send('pepehands lmao! 🐸')
client.run(TOKEN)
