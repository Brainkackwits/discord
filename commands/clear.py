import discord
import asyncio
from functions import permission

async def ex(args, message, client, invoke):
    if permission.check(message,9):
        try:

                 ammount = int(message.content.split(" ")[1])
                 msg = []
                 async for m in message.channel.history(limit=ammount+1):
                     msg.append(m)
                 await message.channel.delete_messages(msg)
                 return_msg = await message.channel.send("Deleted %s messages." % ammount)
                 msg = []
                 async for m in message.channel.history(limit=1):
                     msg.append(m)
                 await asyncio.sleep(4)

                 await message.channel.delete_messages(msg)
        except:
            await message.channel.send("Max value is <100")
