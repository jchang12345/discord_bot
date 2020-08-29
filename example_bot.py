import discord



TOKEN='SOMETHING_SECRET_HAHA_IAINTJHAGINVINTOAJDSFL'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Ignore any messages from the self
    if message.author == client.user:
        return
    # Hello command (basic) 
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    # Options: provide options 
    if message.content.startswith('$options'):
        try:
            choices = message.content.split(' ')
            result = random.choice(choices[1:])
            await message.channel.send('How about ' + result.capitalize() + '?')
        except IndexError:
            await message.channel.send('I need some options, dude')
    # Cursing
    if message.content.startswith('bitch'):
        await message.channel.send('Hello bitch, cussing is bad 4 u')
    # Pepehands 
    if message.content.startswith('pepehands'):
        await message.channel.send('pepehands lmao!')

@client.event
async def on_reaction_add(reaction, user):
    # Bot aggro react
    if reaction.emoji == '🔪':
        msg = 'I see ' + user.name + ' has reacted with a knife. You think you\'re some real slick sh*t, huh?'
        await reaction.message.channel.send(msg)
        await reaction.message.channel.send('You better watch out punk 🤏👀')
    # Pepehands emoji react
    if reaction.emoji == '🐸':
        await reaction.message.channel.send('pepehands lmao! 🐸🤲')
client.run(TOKEN)
