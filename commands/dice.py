import discord
import settings
import random
import os
from functions import discord_library
from functions import permission
def start(client,message):
    if permission.check(message,1):
        msg = []
        for raw,x in enumerate(message.content[1:]):
            try:
                if int(x):
                    msg.append(x)
            except:
                msg.append(message.content[raw+1])
        content = str(msg).replace(",","")[1:-1].replace("'","").replace(" ","")
        faktor= []
        for x in msg:
            try:
                faktor.append(int(x))
            except:
                break
        try:
            numb = int(message.content[int(len(faktor)+2):])
            if content[len(faktor)]=="D" or content[len(faktor)]=="d":
                y = 0
                z = []
                faktor = ''.join(str(e) for e in faktor)
                for x in range(int(faktor)):
                    z.append(x)
                    z[x] = random.randint(1,numb)
                    y = y+z[x]
                return message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description=("Es wurden "+str([(z[x]) for x in range(int(faktor))])[1:-1]+" gewürfelt!"+"\n Das sind "+str(y))))
        except:
            return message.channel.send(embed=discord.Embed(color=discord.Color.red(),description=("ERROR")))
