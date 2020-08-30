import discord
import random 
# import json (for later)? idk 
import discord
from random import randint

TOKEN='SOMETHING_SECRET_HAHA_IAINTJHAGINVINTOAJDSFL'

client = discord.Client()


def humanActions(human_input):
    humanAction=human_input
    if(humanAction=='R'):
        
        return "rock"
    elif(humanAction=='P'):
        
        return "paper"
    elif(humanAction=='S'):
        
        return "scissors"
    else:
        #await message.channel.send('Ok human idk what u sayin')
        return 


#Robot function
def robotActions():
    randomNum_Robot=randint(0, 2)
    listofActions=['rock', 'paper', 'scissors']
    return listofActions[randomNum_Robot]

#who wins the game?
def comparison(humansMove,robotsMove):
    if(humansMove==robotsMove):
        #await message.channel.send('TIED')
        return "TIED"
    elif(humansMove=='rock'):
        if(robotsMove=='paper'):
            #await message.channel.send('PEPE WINS')
            return "PEPE WINS"
        elif(robotsMove=='scissors'):
            #await message.channel.send('YOU WIN')
            return "YOU WIN"
    elif(humansMove=='paper'):
        if(robotsMove=='rock'):
            #await message.channel.send('YOU WIN')
            return "YOU WIN"
        elif(robotsMove=='scissors'):
            #await message.channel.send('PEPE WINS') 
            return "PEPE WINS"
    elif(humansMove=='scissors'):
        if(robotsMove=='rock'):
            return "PEPE WINS"
        elif(robotsMove=='paper'):
            return "YOU WIN"


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

    #rock paper scissors game, still haven't figured out events.
    if message.content.startswith('rps'):
        await message.channel.send('lets play rock paper scissors:')
        await message.channel.send('($R) for Rock, ($P) for Paper, ($S) for Scissors:')
    if message.content.startswith('$R'):
            #humanActions('R')
        await message.channel.send('Human plays Rock')
        humansMove=humanActions('R')
        robotsMove=robotActions()
        #await message.channel.send('pepesadge')
        await message.channel.send('Pepe picks... ')
        await message.channel.send(robotsMove)
        winner=comparison(humansMove,robotsMove)
        await message.channel.send(winner) 
    if message.content.startswith('$P'):
        await message.channel.send('Human plays Paper')
        humansMove=humanActions('P')
        robotsMove=robotActions()
        await message.channel.send('Pepe picks... ')
        await message.channel.send(robotsMove)
        winner=comparison(humansMove,robotsMove)
        await message.channel.send(winner) 
    if message.content.startswith('$S'):
        await message.channel.send('Human plays Scissors')
        humansMove=humanActions('S')
        robotsMove=robotActions()
        await message.channel.send('Pepe picks... ')
        await message.channel.send(robotsMove)
        winner=comparison(humansMove,robotsMove)
        await message.channel.send(winner)  

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



