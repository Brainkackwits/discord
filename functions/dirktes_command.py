import discord
import settings
import os
from functions import discord_library
from functions import permission
def start(client,message):
    #print(message.content[1:])
    faktor = []
    for x in message.content[1:]:
        faktor.append(x)
        #str(returnpermission).replace(',', '\n')[1:-1].replace("'","")
    faktor = str(faktor).replace(",","")[1:-1].replace("'","").replace(" ","")
    print(faktor)
    channel = message.channel
    msg = message.content
    clientprotokoll = client.voice_clients
    invoke = 
    args = msg.split(" ")[1:]
    if commands.__contains__(invoke):
        await commands.get(invoke).ex(args,message,client,invoke)
    else:
        pass
