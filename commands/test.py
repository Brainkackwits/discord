import discord
import praw
import random
reddit = praw.Reddit(client_id="Cfif076KwqKXWQ",
client_secret="o9bTBfEIkhq5LP7s5ryZ07",
user_agent="TEST BOT")
for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)
