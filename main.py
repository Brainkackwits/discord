#!/usr/bin/python3
import discord
import settings
import time
"""TO DO"""
"""musik, -> yt, spotiy -> playlist speichern"""
"""magische miesmuschel"""
"""abstimmungen"""
"""gummizelle"""
from functions import permission, discord_library
from commands import help,permissions,dm_chat,clear,dice,music,meme
client = discord.Client()
#
commands = {
"help":help,
"permission":permissions,
"clear":clear,
"meme":meme,
}
serverdeletelist = []
@client.event
async def on_ready():
    permission.load()
    print(f'{client.user} is logged in successfully.\n')
    for t,s in enumerate(client.guilds):
        if not s.id ==  461201879712399371 and not s.id == 908762450751520828:
                print("Server delete %s %s" % ((s.name,s.id)))
                await s.leave()


        else:
            print("Server joined %s (%s)" % (s.name, s.id))

    await client.change_presence(activity=discord.Game(settings.botdescription))

@client.event
async def on_member_join():
    pass #autorole
@client.event
async def on_message(message):
    channel = message.channel
    msg = message.content
    dm = discord_library.dm_channel(message)

    clientprotokoll = client.voice_clients
    if dm.is_dm_channel(message):
        dm_chat.ex(client,message)
    if msg.startswith(settings.PREFIX):
        global v
        try:#dice&musik
            args = message.content.split

            if msg[1:5]=="join":
                try:
                    await v.join()
                except:
                    v = music.music(client,message)
                    await v.join()
            elif msg[1:5]=="play":
                if args(" ")[1:]:
                    try:
                        await v.play(args(" ")[1:])
                    except:
                        #v = music.music(client,message)
                        await v.play(args(" ")[1:])
                else:
                    await channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                            "*play title")))
            elif msg[1:6]=="leave":
                await v.leave()
            elif msg[1:5]=="stop":
                await v.stop()


            elif int(message.content[1:2]):
                    await dice.start(client,message)

        except ValueError:
            invoke = msg[len(settings.PREFIX):].split(" ")[0]
            args = msg.split(" ")[1:]
            #print("error "+str(IOError))
            if commands.__contains__(invoke):
                await commands.get(invoke).ex(args,message,client,invoke)
            else:#class error
                await channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                        "The command `%s` is not valid!" % invoke)))

client.run(settings.Token)
