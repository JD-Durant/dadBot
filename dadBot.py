import discord
from discord.ext import commands
token = "" #Pop your token in here and dadbot is off!
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
words = ["i'm", "i am", "im ", "i;m"]
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))
    print(f"{client.user.name} has connected to Discord.")

@client.event
async def on_message(message):
    lowerCaseMessage = str(message.content.lower())
    if message.author != client.user:
        if message.author == message.guild.owner:
            return
        if message.mention_everyone:
            await message.reply("Funny one there bud, better luck next time")
            return
        for word in words:
            if word in lowerCaseMessage:
                funnyDadJoke = lowerCaseMessage.split(word, 1)[1]
                try:
                    if len(funnyDadJoke) > 32:
                        await message.author.edit(nick="insertDadJokeHere")
                    else:
                        await message.author.edit(nick=f"{funnyDadJoke}")
                except:
                    await message.channel.send("Hey! That's lame! Let me change nicknames >:(")
                    break
                await message.reply(f"Hi {funnyDadJoke}, I'm Dad.")
                break

client.run(token)
