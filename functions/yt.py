import os
import subprocess
import re
import discord
from pytube import YouTube
from pytube import Playlist
import glob
try:
    import settings
except:pass
YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
try:
    DOWNLOAD_DIR = settings.path+'\\musik\\queue'
except:
    DOWNLOAD_DIR = "F:\\project's\\discord\\musik\\queue"
def ex(title,message):
    try:
        try:
            playlist = Playlist(title)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            for url in playlist.video_urls:
                print(url)
                yt = YouTube(url)

                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path=DOWNLOAD_DIR)

                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                print(yt.title + " has been successfully downloaded.")


        except:

            yt = YouTube(title)

            video = yt.streams.filter(only_audio=True).first()



            out_file = video.download(output_path=DOWNLOAD_DIR)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print(yt.title + " has been successfully downloaded.")
    except:
        yield from message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=("Video konnte nicht gefunden werden")))



















    """play = Playlist(str(title))
    play._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for url in play.video_urls:
        yt = YouTube(url)
        print(url)
        audio = yt.streams.get_audio_only()
        audio.download(DOWNLOAD_DIR)"""
#ex("https://www.youtube.com/watch?v=gQG_2O9Bu6c&list=PL3-sRm8xAzY9sDilvaWjCwCI0TkUzYdOG")
"""for name in glob.glob(DOWNLOAD_DIR+'\\*'):
    print(name)"""
