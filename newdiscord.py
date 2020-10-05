import discord
import openpyxl
import requests
import asyncio
import random
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("노력")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("폴러야 안녕"):
        await message.channel.send("안녕하세요")

    if message.content.startswith("폴러야 뭐해"):
        await message.channel.send("폴러는 공부하는중")

    if message.content.startswith("폴러야 명령어"):
        await message.channel.send("폴러야")

    if message.content.startswith("wood hi"):
        await message.channel.send("hihi")

    if message.content.startswith("wood babo"):
        await message.channel.send("nooo")

    if message.content.startswith("wood status"):
        await message.channel.send("wood is studying")



client.run("NjY1OTMxMTQwNjkxMDAxMzU1.XhsytA.dcBTC5dNdJNiPsd6kUClL--AHU8")
