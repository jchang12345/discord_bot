
import discord
import json
import re
import random 

from random import randint


#voice class discord.VoiceClient
#voice =discord.VoiceClient

#src=await discord.FFMpegOpusAudio.from_probe("swiftaswind.mp3")
#voice.play(src)



#client class discord.Client()



#TOKEN='OOPS I FORGOT IT WAS NOT SUPPOSED TO BE UPLOADED'
client = discord.Client()
champJSON = open('champion.json', 'r')
champDict = json.loads(champJSON.read())['data']

# Helper function for RPS
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

    ##tts stuff
    if message.content.startswith('$tts'):
        try:
            ans = message.content.split(' ')[1:]

            await message.channel.send(content=ans,tts=True)
        except IndexError:
            await message.channel.send('\$tts <desired tts msg>')
    if message.content.startswith('$test_tts'):
        await message.channel.send(content='stop it you baka', tts=True)
    # Ignore any messages from the self
    if message.author == client.user:
        return
    # Hello command (basic) 
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    # Cursing
    if message.content.startswith('bitch'):
        await message.channel.send('Hello bitch, cussing is bad 4 u')
    # Pepehands 
    if message.content.startswith('pepehands'):
        await message.channel.send('pepehands lmao!')
    # Options command: Provide options and have one picked
    if message.content.startswith('$option'):
        try:
            choices = message.content.split(' ')
            result = random.choice(choices[1:])
            await message.channel.send('Let\'s go with ' + result.capitalize() + '! GLHF! 🤪')
        except IndexError:
            await message.channel.send('I need some options, dude 🤡')


    #rock paper scissors game, event + only R P S if rps starts
    if message.content.startswith('rps'):
        await message.channel.send('lets play rock paper scissors:')
        await message.channel.send('(R) for Rock, (P) for Paper, (S) for Scissors:')
        msg=''
        def check_rps(m):
            #await message.channel.send(m)
            return m
        msg2=await client.wait_for('message',check=check_rps) 
        await message.channel.send('Hello {.author}!'.format(msg2))
        await message.channel.send('nice you played')
        msg=msg2.content
        if msg=='R':
            msg='Rock'
        elif msg=='P':
            msg='Paper'
        elif msg=='S':
            msg='Scissors'
        else:
            msg='bro... 🤡??! (R) or (P) or (S)! please try again...'
        await message.channel.send(msg)   
        if msg=='Rock':
            #humanActions('R')
            await message.channel.send('Human plays Rock')
            humansMove=humanActions('R')
            robotsMove=robotActions()
            #await message.channel.send('pepesadge')
            await message.channel.send('Pepe picks... ')
            await message.channel.send(robotsMove)
            winner=comparison(humansMove,robotsMove)
            await message.channel.send(winner) 
        if msg=='Paper':
            await message.channel.send('Human plays Paper')
            humansMove=humanActions('P')
            robotsMove=robotActions()
            await message.channel.send('Pepe picks... ')
            await message.channel.send(robotsMove)
            winner=comparison(humansMove,robotsMove)
            await message.channel.send(winner) 
        if msg=='Scissors':
            await message.channel.send('Human plays Scissors')
            humansMove=humanActions('S')
            robotsMove=robotActions()
            await message.channel.send('Pepe picks... ')
            await message.channel.send(robotsMove)
            winner=comparison(humansMove,robotsMove)
            await message.channel.send(winner)  



    # Role command: Pick a role/category and have a random option 
    if message.content.startswith('$role'):
        try:
            ans = message.content.split(' ')[1]
            choices = []
            role = ''

            # Check the input for each type of role 
            if re.search('[aA]ssassin', ans):
                role = 'Assassin'
            elif re.search('[fF]ighter', ans) or re.search('[mM]elee', ans):
                role = 'Fighter'
            elif re.search('[mM]ag.*', ans):
                role = 'Mage'
            elif re.search('[mM]id.*',ans):
                role= 'Mage'
            elif re.search('[mM]ark.*', ans) or re.search('[aA][dD][cC]', ans):
                role = 'Marksman'
            elif re.search('[sS]up.*', ans):
                role = 'Support'
            elif re.search('[tT]ank', ans):
                role = 'Tank'
            else:
                await message.channel.send('Are you sure you picked a real role? So far, the only supported types are assassin, fighter, mage/mid, marksman/adc, support, and tank.🤡')

            # Loop through dictionary, get any champID that has the role 
            for champ in champDict:
                if role in champDict[champ]['tags']:
                    choices.append(champ)
            # Choose and send result
            result = random.choice(choices)
            resName = champDict[result]['name']
            resTitle = champDict[result]['title']
            await message.channel.send('Let\'s go with ' + resName + ', ' + resTitle + '! GLHF! 🤠')
        except IndexError:
            await message.channel.send('\$role <desired role>')

    # Randomized champion pick -- ARAM without the AM! (Also have to have the champ lol)
    if message.content.startswith('$rand'):
        randChamp = random.choice(list(champDict.items()))[1]
        randChampName = randChamp['name']
        randChampTitle = randChamp['title']
        await message.channel.send('Your completely random pick is ' + randChampName + ', ' + randChampTitle +'! GLHF! 🤩')



@client.event
async def on_reaction_add(reaction, user):
    # Bot aggro react
    if reaction.emoji == '🔪':
        await reaction.message.channel.send('I see ' + user.name + ' has reacted with a knife. You think you\'re some real slick sh*t, huh?\n You better watch out punk 🤏👀')
    # Pepehands emoji react
    if reaction.emoji == '🐸':
        await reaction.message.channel.send('pepehands lmao! 🐸🤲')

client.run(TOKEN)


