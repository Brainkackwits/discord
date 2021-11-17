import discord
import settings
import os,time
from functions import discord_library,downtube
from functions import permission,music
import threading

async def ex(args,message,client,invoke):
    voice = music.stats.voice(client)
    auto = threading.Thread(target=autoplay,args=(args,message,client,invoke,voice,))
    if permission.check(message,2):

        if message.content.startswith(settings.PREFIX+"play") or message.content.startswith(settings.PREFIX+"Play"):
            if len(args[0]) >= 2:

                await music.join(args,message,client,invoke,music.stats.voice(client))
                queue,index = await downtube.downtube(args[0]).downloader()

                if music.stats.voice(client).is_playing():
                    await music.move(voice,message)
                else:
                    #thread autoplay
                    auto.start()
                    #music.stats.voice(client).play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(queue[index])))

            else:
                await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                    "*play song")))
        if message.content.startswith(settings.PREFIX+"join") or message.content.startswith(settings.PREFIX+"Join"):
            await music.join(args,message,client,invoke,voice)
        if message.content.startswith(settings.PREFIX+"skip") or message.content.startswith(settings.PREFIX+"Skip"):
            music.stats.run = False
            music.stats.voice(client).stop()
            try:
                if int(args[0]) >= 1:
                    music.stats.index = music.stats.index + int(args[0])-1
            except:pass
            if not music.stats.run:
                music.stats.run = True
                auto.start()
            #music.stats.voice(client).play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(music.stats.queue[music.stats.index])))
        if message.content.startswith(settings.PREFIX+"return") or message.content.startswith(settings.PREFIX+"Return"):
            music.stats.run = False

            music.stats.voice(client).stop()
            try:
                if int(args[0]) >= 1:
                    music.stats.index = music.stats.index - int(args[0])-1
            except:music.stats.index = music.stats.index -2
            if not music.stats.run:
                music.stats.run = True
                auto.start()
            #voice.play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(music.stats.queue[music.stats.index])))
        if message.content.startswith(settings.PREFIX+"leave") or message.content.startswith(settings.PREFIX+"Leave"):
            print("leave")
        if message.content.startswith(settings.PREFIX+"queue") or message.content.startswith(settings.PREFIX+"Queue"):
            if len(music.stats.queue) >= 10:
                index = 10
            else:
                index = len(music.stats.queue)
            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description=("playing... "+str(music.stats.queue[music.stats.index-1])[12:-4])))
            await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description=(str([x[12:-4] for x in music.stats.queue[music.stats.index-2:index]])[2:-2].replace("', '","\n"))))
        if message.content.startswith(settings.PREFIX+"stop") or message.content.startswith(settings.PREFIX+"Stop"):
            music.stats.run = False
            music.stats.voice(client).stop()
        if message.content.startswith(settings.PREFIX+"add"):
            print("add")#add name of playlist
def autoplay(args,message,client,invoke,voice):
    while music.stats.run:
        time.sleep(1)
        if len(music.stats.queue) >= 1 and len(music.stats.queue) >= music.stats.index:
            if not music.stats.voice(client).is_playing():
                music.stats.voice(client).play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(music.stats.queue[music.stats.index])))
                music.stats.index = music.stats.index+1
