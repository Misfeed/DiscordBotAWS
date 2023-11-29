'''import class libraries to interact with discord, import the token file,
 interact with operating system and randomly generate something '''

import discord
import os
import random
from ec2_metadata import ec2_metadata

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#from dotenv import load_env. Folder structure importing the token string

#Creation of client object from the discord class, Bot subclass.
#Insert the token for OAuth 2

client = discord.Bot()
token = str(os.getenv('TOKEN'))

'''Event Driven'''

@client.event
async def on_ready():
    print("Logged in as bot {0.user}".format(client))

'''Event driven by '''

@client.event
async def on_message(message):
    username = str(message.author).split
    channel = str(message.channel.name)
    user_message = str(message.content)

#outtput,format{f} with brackets.
print(f'Message {user_message} by {username} on {channel}')

#client user is the bot right? is the user is the bot.
if message.author == client.user:
    return

'''If the channel name is random run'''

if channel == "random":
    if user_message.lower() == "boomer?" or user_message.lower() == "boomer?":
        await message.channel.send(f"{username} Your EC2 Data: {ec2_metadata.region}") #format of string
        return
    
    #other string options
    elif user_message.lower() == "hello?":
        await message.channel.send(f'Sooner!{username}')
    
    #Returning instance data for the last conditional statement.
    elif user_message.lower() == "EC2 Data":
        await message.channel.send("Your instance data is" + ec2_metadata)

#Start execution by passing the token object.
client.run(token)