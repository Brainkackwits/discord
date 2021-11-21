import discord
import settings
import os,time,random
from functions import discord_library,downtube
from functions import permission,music
import threading

async def ex(args,message,client,invoke):
    voice = music.stats.voice(client,message)
    auto = threading.Thread(target=autoplay,args=(args,message,client,invoke,voice,))
    if permission.check(message,2):

        if message.content.startswith(settings.PREFIX+"play") or message.content.startswith(settings.PREFIX+"Play"):
            try:
                if args[0].startswith("*add"):#add name of playlist
                   try:
                        if len(args[1]) >= 2:
                            playlist = music.playlist(args[1],message)
                            playlistvalue = {}
                            #value = music.stats.queue#dict->{queueindex:url} import from queue
                            for raw,value in enumerate(music.stats.queue):
                                playlistvalue[raw] = value
                            playlist.write(playlistvalue)

                   except:
                       await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                           "*play *add Playlistname\n*play *playlistlist\n*play *playlistname")))
                elif args[0].startswith("*"):
                    #print(settings.path+"musik\\playlist\\"+args[0].split("*")[1]+".json")
                    playlist = music.playlist(args[0].split("*")[1],message)
                    #print(list(playlist.read().values())[1:])
                    music.stats.queue.extend(list(playlist.read().values())[1:])
                    await music.join(args,message,client,invoke,music.stats.voice(client,message))
                    #print(music.stats.queue)
                    #music.stats.run = False
                    #music.stats.voice(client,message).stop()
                    if not music.stats.voice(client,message).is_playing():
                        music.stats.run = True
                        auto.start()
                elif len(args[0]) >= 2:
                    await music.join(args,message,client,invoke,music.stats.voice(client,message))
                    await downtube.downtube(args[0]).downloader()

                    if music.stats.voice(client,message).is_playing():
                        await music.move(voice,message)
                    else:
                        #thread autoplay
                        auto.start()
                        #music.stats.voice(client).play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(queue[index])))

                else:
                    await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                        "*play song")))
            except:pass

            #try:

            #except:
                #await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                    #"*play song\n*play *add")))
        if message.content.startswith(settings.PREFIX+"join") or message.content.startswith(settings.PREFIX+"Join"):
            await music.join(args,message,client,invoke,voice)
        if message.content.startswith(settings.PREFIX+"skip") or message.content.startswith(settings.PREFIX+"Skip"):
            music.stats.run = False
            music.stats.voice(client,message).stop()
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

            music.stats.voice(client,message).stop()
            try:
                if int(args[0]) >= 1:
                    music.stats.index = music.stats.index - int(args[0])-1
            except:music.stats.index = music.stats.index -2
            if not music.stats.run:
                music.stats.run = True
                auto.start()
        if message.content.startswith(settings.PREFIX+"leave") or message.content.startswith(settings.PREFIX+"Leave"):
            print("leave")
        if message.content.startswith(settings.PREFIX+"queue") or message.content.startswith(settings.PREFIX+"Queue"):
            if len(music.stats.queue) >= 10:
                index = 10
            else:
                index = len(music.stats.queue)
            await message.channel.send(embed=discord.Embed(color=discord.Color.orange(),description=(str([queue[len(settings.path)+15:-4] for queue in music.stats.queue[music.stats.index-1:music.stats.index]])[2:-2]).replace("', '","\n")).set_author(name="playing... "))
            await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description=(str([queue[len(settings.path)+15:-4] for queue in music.stats.queue[music.stats.index:]])[2:-2]).replace("', '","\n")))
        if message.content.startswith(settings.PREFIX+"stop") or message.content.startswith(settings.PREFIX+"Stop"):
            music.stats.run = False
            music.stats.voice(client,message).stop()
        if message.content.startswith(settings.PREFIX+"shuffle") or message.content.startswith(settings.PREFIX+"Shuffle"):
            #print(music.stats.queue[music.stats.index:])
            #print()
            perm = list(range(len(music.stats.queue[music.stats.index:])))
            random.shuffle(perm)
            now = music.stats.queue[music.stats.index-1]
            music.stats.queue = [music.stats.queue[index] for index in perm]
            music.stats.queue[music.stats.index-1] = now
            #print(music.stats.queue[music.stats.index:])
def autoplay(args,message,client,invoke,voice):
    while music.stats.run:
        time.sleep(1)
        if len(music.stats.queue) >= 1 and len(music.stats.queue) >= music.stats.index:
            if not music.stats.voice(client,message).is_playing():
                music.stats.voice(client,message).play(discord.FFmpegPCMAudio(executable=settings.path+"\\ffmpeg.exe",source=(music.stats.queue[music.stats.index])))

                try:
                    music.stats.index = music.stats.index+1
                except:pass
