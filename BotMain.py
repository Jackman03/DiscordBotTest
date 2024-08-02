import discord
import datetime as dt
from discord.ext import commands
import os
from dotenv import load_dotenv
from BotLogs import *
import requests
def Configure():
    load_dotenv()

ChanelID = os.getenv('Key')
#the start of a command prefix. when a user types a ! the bot will be registered
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
#sets up first command
async def on_ready():
    print("Bot is loaded")

#ping pong command
@client.command()
async def Ping(ctx):
    #take input from discord
    await ctx.send("Pong")
    LogCommand("Ping",{ctx.author.name})

@client.command()
async def Help(ctx):
    await ctx.send("This is the list of commands:")
    await ctx.send("!Ping - Displays Pong as a reply")
    await ctx.send("!Hello - Says hello to the user")
    await ctx.send("!Wiki - Gets a random wikipedia article")
    LogCommand("Help",{ctx.author.name})

#gets a random wikipedia article
@client.command()
async def Wiki(ctx):
    baseurl = "https://en.wikipedia.org/wiki/Special:Random"
    r = requests.get(baseurl)
    #uses the requests libary to send a http get to the url, then sends back a random article

    await ctx.send(r.url)
    LogCommand("Wiki",{ctx.author.name})
    

#hello command
@client.command()
async def Hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}")
    LogCommand("Hello",{ctx.author.name})
    

#user has joined event
@client.event
async def on_member_join(member):
    channel = client.get_channel(ChanelID)
    await channel.send(f"Hello! Welcome to the server {member.author.name}")
    LogMemberFluctation("joined",{member.author.name})

#user has left event
@client.event
async def on_member_remove(member):
    print("member has joined")
    channel = client.get_channel(ChanelID)
    await channel.send("Goodbye!")
    LogMemberFluctation("left",{member.author.name})



Configure()
client.run(os.getenv('Key'))