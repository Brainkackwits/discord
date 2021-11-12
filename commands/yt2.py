# importing packages
from pytube import YouTube
from pytube import Playlist
import os
import re
destination = "F:\\project's\\discord\\musik\\queue"
mainurl = str(input("Enter the URL of the video you want to download: \n>> "))
try:
    playlist = Playlist(mainurl)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for url in playlist.video_urls:
        print(url)
        yt = YouTube(url)

        video = yt.streams.filter(only_audio=True).first()



        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " has been successfully downloaded.")
except:
    yt = YouTube(mainurl)

    video = yt.streams.filter(only_audio=True).first()



    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")
