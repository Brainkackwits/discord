import discord
import settings
import os
from functions import discord_library
from functions import permission
def ex(args,message,client,invoke):
    if permission.check(message,10):
        dm = discord_library.dm_channel(message)
        args = message.content.split
        if dm.is_dm_channel():
            return dm.send(embed=discord.Embed(color=discord.Color.red(), description=("Dieser Befehl funktioniert nur auf einem Server auf dem der Bot Installiert ist!")))
        returnpermission = permission.__return(client,message)
        if args("return")[1:]:
            return message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                    "This all Permissions \n`%s` " % str(returnpermission).replace(',', '\n')[1:-1].replace("'",""))))
        elif args("set")[1:]:
            if len(args(" ")) >= 4:
                if int(args(" ")[2]) in permission.__returnid__(client,message.channel) and int(args(" ")[3]) >= 0:
                    newjson = {
                    str(args(" ")[2]):int(args(" ")[3]),
                    }
                    if os.path.isfile(settings.path+"\\permissions.json"):#exist file
                        change = open(settings.path+"\\permissions.json",'r')#readfile
                        oldjson = change.read()
                        change.close()
                        f = open(settings.path+"\\permissions.json",'w')#clear file
                        f.close()
                        f = open(settings.path+"\\permissions.json",'a')#newfile
                        if len(oldjson) >= 5:#content?
                            length = len(oldjson.split(","))

                            #print(oldjson.split(","))#-> roleid:permissionid,'\n'
                            for x in oldjson.split(","):
                                y = x.split(":")
                                if not str(args(" ")[2]) == x.split(":")[0]:#not roleid == contentid?
                                    if not x =='':
                                        f.write(str(y[0])+":"+str(y[1])+",")
                                        #print(str(y[0])+":"+str(y[1])+",")
                                else:
                                    f.write(args(" ")[2]+":"+args(" ")[3]+",")#permission change
                                    #print(args(" ")[2]+":"+args(" ")[3]+",")
                            if not args(" ")[2] in oldjson:
                                f.write(str(args(" ")[2])+":"+str(args(" ")[3])+",")
                        else:
                            f.write(str(args(" ")[2])+":"+str(args(" ")[3])+",")
                            #print(str(args(" ")[2])+":"+str(args(" ")[3]))
                        f.close()
                        #await message.channel.send("Datei wurde erstellt!")
                    else:
                        open(settings.path+"\\permissions.json",'x')
                        return message.channel.send("Datei wurde erstellt!")
                        pass

                    return message.channel.send("Erfolgreiche änderung")
                return message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=(
                "Diese Role gibt es nicht")))

            else:
                return message.channel.send(embed=discord.Embed(color=discord.Color.blue(), description=(
                "PREFIX permission return -> List of Roles\n PREFIX permission set role.id perlvl=(0-10)")))
        elif args("idlist")[1:]:
            f = open(settings.path+"\\permissions.json",'r')
            return message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description=(str(f.read()).replace(',', '\n'))))
            f.close()
        elif args("namelist")[1:]:
            f = open(settings.path+"\\permissions.json",'r')
            #print(permission.__return(client,message.channel))
            names = ([(y.split(":")[0]+" "+x.split(":")[1]) for x in f.read().split(",") if x != "" for z in returnpermission for y in z.split(",") if x.split(":")[0] in y.split(":")[1]])

            return message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description=(str(names).replace(',', '\n')[1:-1].replace("'",""))))
            f.close()
        else:
            return message.channel.send(embed=discord.Embed(color=discord.Color.blue(), description=(
            "*permission return -> List of Roles\n *permission set role.id perlvl=(0-10)\n *permission idlist\n *permission namelist")))
    else:
        return message.channel.send("Du besitzt keine Berechtigungen!")
