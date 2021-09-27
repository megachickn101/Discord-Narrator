import discord
from discord.ext import commands
from discord.utils import get
import os
from gtts import gTTS
import playsound
import time

intents = discord.Intents.default()
client = commands.Bot(command_prefix = 'dn ', intents=intents)

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def is_it_me(ctx):
	return ctx.author.id == USERID

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Insert Status Message*'))
	print('Narrator Is Online')ss
	time.sleep(20)

@client.event
async def on_message(message):
    speak(f"In {message.guild} in {message.channel}, {message.author.name} said {message.content}.")
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.author.id}: {message.content}: {message.guild}: {message.guild.id}")
    await client.process_commands(message)

@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
	await client.close()

@client.command()
@commands.check(is_it_me)
async def fshutdown(ctx):
	await client.close()


client.run("TOKEN")
