import discord
import asyncio
class playlist:
    def __init__(self):
        pass

class stats:
    queue = []
    index = 0
    run = True
    def voice(client):
        index = 1
        return discord.utils.get(client.voice_clients, guild=client.guilds[index])




async def join(args,message,client,invoke,voice):
        try:

            try:
                voicechannel = discord.utils.get(message.guild.voice_channels, name=args[0])
                await voicechannel.connect()
            except:
                voicechannel = discord.utils.get(message.guild.voice_channels, name=message.author.voice.channel.name)
                await voicechannel.connect()
                stats = music.stats(client)
        except:
            try:
                await move(voice,message)

            except:
                pass#error
async def move(voice,message):
    if voice.is_connected():
        try:#move
            voicechannel = discord.utils.get(message.guild.voice_channels, name=message.author.voice.channel.name)
            await voice.move_to(voicechannel)
        except:
            voicechannel = discord.utils.get(message.guild.voice_channels, name=args[0])
            await voice.move_to(voicechannel)
