import discord
import praw
import random
async def ex(args,message,client,invoke):
    reddit = praw.Reddit(client_id="4Cmef8S80YcQIg",
    client_secret="	dDfmh8Em9liofN5q6nBN-cmmoCuqPg",
    user_agent="TEST BOT")
    #print(reddit.read_only)
    #memes_sub = reddit.subreddit("memes").hot()
    #post_to_pick = random.randint(1, 100)
    #for i in range(0, post_to_pick):
        #sub = next(x for x in memes_sub if not x.sticky())
    for submission in reddit.subreddit("learnpython").hot(limit=10):
        print(submission.title)
    #await message.channel.send(memes_sub)
