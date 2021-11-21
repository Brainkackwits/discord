import discord
import asyncio
import glob
import settings
import json,time
class playlist:
    def __init__(self):
        pass

class stats:
    queue = []
    index = 0
    run = True
    login_server = None
    #playlistfiles = glob.glob(settings.path+"musik\\playlist\\*.mp3")
    queuelistfiles = glob.glob(settings.path+"musik\\storage\\*.mp3")
    def voice(client,message):
        """for guild in range(len(client.guilds)):
            try:
                stats.login_server = discord.utils.get(client.voice_clients, guild=guild)

            except:pass"""
        return discord.utils.get(client.voice_clients, guild=message.author.guild)



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
    def __init__(self,title=None,message=None):
        self.author = message.author.name
        if not "musik\\playlist\\"+title+".json" in glob.glob("musik\\playlist\\*.json") and title != None:
            self.title = self._create(title)
        else:
            self.title = "musik\\playlist\\"+title+".json"



    def _create(self,title):
        self.file = open("musik\\playlist\\"+title+".json", "w")
        self.file.write(json.dumps({"author":self.author}))
        self.file.close()
        return "musik\\playlist\\"+title+".json"
    def read(self):
        with open(self.title, 'r') as self.loadfile:
            self.data = json.load(self.loadfile)
            self.loadfile.close()
            return self.data

    def write(self,filepath):
        data = self.read()
        for raw,key in enumerate(filepath.keys()):
                data[key]=[x for x in filepath.values()][raw]
        if self.author == data["author"] and dict(filepath):
            with open(self.title, 'w') as self.writefile:
                json.dump(data,self.writefile)
                self.writefile.close()

#data = {"name":"url","1":"two"}

#playlist("title").write(data)
