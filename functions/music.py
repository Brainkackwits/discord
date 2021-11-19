import discord
import asyncio
import glob
import settings
class playlist:
    def __init__(self):
        pass

class stats:
    queue = []
    index = 0
    run = True
    #playlistfiles = glob.glob(settings.path+"musik\\playlist\\*.mp3")
    queuelistfiles = glob.glob(settings.path+"musik\\storage\\*.mp3")
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
class playlist:
    def __init__(self,title=None,name=None):
        self.title = title
        if title == None:
            self.title =self._create(name)

    def add_queue(self):
        pass
    def _create(self,name):
        return name
