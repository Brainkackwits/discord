class stats:
    volume = 100
    voiceclient = None
    def voice(x):voiceclient=x
import discord
import settings
import glob
import os
import asyncio
import time
import threading
from functions import yt
class playlist:
    def __init__(self,plist=[]):
        self.plist = plist
        self.index = 0
    def update(self,plist):
        self.plist = plist
    def next(self):
        self.index = self.index +1
    def back(self):
        self.index = self.index -1
    def get(self):
        if len(self.plist) >= self.index:
            return self.plist[self.index]
        return False

    def save(self):pass
class music:
    def __init__(self,client,message):
        self.client = client
        self.message = message
        self.p = True
    def source(self):
        return self.voiceclient.source()
    async def send_packet(self,data=settings.path+"\\musik\\test.mp3"):
        await self.voiceclient.send_audio_packet(data)#encode by opus
    def stuffle(self):pass
    def save(self):pass
    def _playing(self):
        while self.p:
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(self.playing())
            except:pass
            #await self.playing()
    async def playing(self):
        if not self.voice.is_playing():
            self.voice.play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=self.plist.get()))
            await self.message.channel.send(embed=discord.Embed(color=discord.Color.gold(), description=("is playing {}".format(self.plist.get()[37:-4]))))
            self.plist.update(glob.glob(settings.path+'\\musik\\queue\\*'))
            print(self.plist.get())
            self.plist.next()

        elif type(self.plist.get()) == bool:
            await self.message.channel.send(embed=discord.Embed(color=discord.Color.gold(), description=("Playlist end")))

    async def join(self):
        if not self.message.author.voice.channel:
            await message.channel.send("You're not connected to any voice channel !")
        else:
            self.voice = discord.VoiceClient(client=self.client,channel=self.message.author.voice.channel)
            if self.client.user.name in [(x.name) for c in self.client.guilds for y in c.voice_channels for x in y.members]:
                if self.voice and self.voice.is_playing():
                    try:
                        await self.voice.move_to(self.message.author.voice.channel)
                    except:
                        return self.voice
                else:
                    self.voice = await self.message.author.voice.channel.connect()
            else:
                self.voice = await self.message.author.voice.channel.connect()
    async def stop(self):
        self.p = False
        self.voice.pause()
    async def leave(self):
        await self.voice.disconnect()
    async def play(self,title):
        await self.join()
        self.p = True
        threading.Thread(target=yt.ex,args=(title,self.message)).start()
        self.plist = playlist(glob.glob(settings.path+'\\musik\\queue\\*'))
        while not self.plist.get():
            self.plist(glob.glob(settings.path+'\\musik\\queue\\*'))

        threading.Thread(target=self._playing).start()
