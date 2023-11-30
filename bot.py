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



@client.event
async def on_ready():
    print("Logged in as bot {0.user}".format(client))



@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    choices = ("time","what is the downtime","downtime")

    while user_message not in choices:
        user_message = message.channel.send(f'Please ask for "downtime" or "time"' {username})

    #outtput,format{f} with brackets.
    print(f'Message {user_message} by {username} on {channel}')

    #client user is the bot right? is the user is the bot.

    if message.author == client.user:
        return 

    if channel == "updates":
        if user_message.lower() == "downtime" or user_message.lower() == "what is the downtime":
            await message.channel.send(f'Downtime is set for 12/25! {username} Your EC2 Data: {ec2_metadata.region}') #format of string
            return
        elif user_message.lower() == "time":
            await message.channel.send(f'12am 12/25! {username}')
        
        #Returning instance data for the last conditional statement.
        elif user_message.lower() == "EC2 Data":
            await message.channel.send("Your instance data is" + ec2_metadata)

#Start execution by passing the token object.
client.run(token)