class dm_channel:
    def __init__(self,message):
        self.message = message
    def is_dm_channel(self,message=None)->bool:
        try:
            if message == None:return self.message.channel.id == self.message.author.dm_channel.id
            else:return message.channel.id == message.author.dm_channel.id
        except:
            return False

    def send(self,message=None,msg=""):
        if not message == None: return self.message.author.send(msg)
        else: return message.author.send(msg)
class channel:
    def __init__(self,message,channel):
        self.message = message
        self.channel = channel
    def send(message=None,channel=None,msg=""):
        if not message == None and not channel == None: return self.message.channel.send(msg)
        elif not channel == None: return message.channel.send(msg)
        elif not message == None: return channel.send(msg)
