import discord
import json
import settings
def check(message,value)->int:
    f = open(settings.path+"\\permissions.json",'r')
    userroleid = message.author.top_role.id
    userid = message.author.id
    y =  f.read().split(",")
    f.close()
    if userid in settings.admins:
        return value <= 12
    for x in y:
        if str(userroleid) in x.split(":")[0]:
            return value <= int(x.split(":")[1])
    return value <= int(0)
def __return__(client,message)->list:
    roles = []
    for role in message.guild.roles:
        roles.append(role.name)
    return roles
def __returnid__(client,channel)->list:
    roles = []
    for guild in client.guilds:
        for role in guild.roles:
            roles.append(role.id)
    return roles
def __return(client,channel):
    roles = []
    roleid = __returnid__(client,channel)
    for x,role in enumerate(__return__(client,channel)):
        roles.append(str(role)+":"+str(roleid[x]))
    return roles

def load():
    pass
